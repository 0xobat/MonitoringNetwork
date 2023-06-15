import board, busio, digitalio
import threading
import adafruit_rfm9x
import time, json
from store import data_store, data_clean, Fault_log, dashboardData
from test.display import Display
from server import run_server, check_values


#===============#
#Use data_clean()
#===============#

#Define Flags
channel_sel = False
data_ack = False


# Initiatize pins and objects
def  setup():
    global rfm9x
    #RFM95 and display pins(maybe)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs =digitalio.DigitalInOut(board.CE1)
    reset = digitalio.DigitalInOut(board.D25)
    g0 = digitalio.DigitalInOut(board.D24)

    # Initialize objects
    rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
    #Initialize rfm9x parameters
    rfm9x.enable_crc = True #Enable CRC Checking
    rfm9x.node = 0   # Central hub address

    #clear and refresh display
    check_values()
    server_run_thread = threading.Thread(target=run_server)
    server_run_thread.daemon = True
    server_run_thread.start()


#Channel selection
def Channel_sel():
    global ch_sel
    ch_sel = False
    print('Listening for Request')
    channel_req_byte = rfm9x.receive(timeout=20.0)  #listen for node request
    if channel_req_byte is not None:
         channel_req = channel_req_byte.decode('utf-8')
         if int(channel_req[0]) == 1:
            rfm9x.destination = 1
            rfm9x.send('Ch1 ACK'.encode('utf-8'))
            print('Ch1 ACK sent')
            ch_sel = True
         elif int(channel_req[0]) == 2:
            rfm9x.destination = 2
            rfm9x.send('Ch2 ACK'.encode('utf-8'))
            print('Ch2 ACK sent')
            ch_sel = True
         else:
            rfm9x.destination = 255
            print("sent to all")
            ch_sel = False
    else:
         print('Channel Select Failed')
         ch_sel = False

#Receive packet from sensor node
def rx_data():
    global data_ack, temp, moist
    data_ack = False
    moist = 0
    temp = 0
    print('Listening for data...')
    sens_data_byte = rfm9x.receive(timeout=5.0)
    if sens_data_byte is not None:
        sens_data = sens_data_byte.decode('utf-8')
        print('Received: {0}'.format(sens_data))
        data_list = json.loads(sens_data)
        data_dict = data_list[0]
        temp = data_dict["Temperature"]
        moist = data_dict["Soil Moisture"]
        if moist or temp != 0:
            rfm9x.send("Data ACK".encode('utf-8')) # send ACK
            data_ack = True
            return sens_data
    else:
        print('Data NOT recieved')
        data_ack = False
        return 0

#Listen for any fault data
def RxFault():
    print('Listening for Fault data...')
    fault_data_byte = rfm9x.receive(timeout=5.0)
    if fault_data_byte is not None:
        rfm9x.send("Fault ACK".encode('utf-8')) # send ACK
        fault_data = fault_data_byte.decode('utf-8')
        print('Received: {0}'.format(fault_data))
        return fault_data
    else:
        print('No Fault Data recieved')

def Rfm9x_sleep(sleep_time):
    rfm9x.sleep()
    time.sleep(sleep_time)
    rfm9x.sleep()

def Channel_Selection():
    global ch_sel, data_ack, temp, moist, rfm9x, node1, node2
    Channel_sel()   #Listen for node requests
    if ch_sel:
        data = rx_data() # Receive sensor data
        if not data_ack:
            data = rx_data()
            if data_ack:
                fault = RxFault() # Listen for previous fault data
                #update csv files
                if rfm9x.destination == 1:
                    data_store(data, 'node1.csv')
                    if len(fault) != 0:
                        data_store(fault,'node1.csv')
                    node1 = True
                elif rfm9x.destination == 2:
                    data_store(data, 'node2.csv')
                    if len(fault) != 0:
                        data_store(fault,'node2.csv')
                    node2 = True
        else:
            fault = RxFault() # Listen for previous fault data
            #update csv files
            if rfm9x.destination == 1:
                data_store(data, 'node1.csv')
                if len(fault) != 0:
                    data_store(fault,'node1.csv')
                node1 = True
            elif rfm9x.destination == 2:
                data_store(data, 'node2.csv')
                if len(fault) != 0:
                    data_store(fault,'node2.csv')
                node2 = True
    else:   # Retry channel Selection
        Channel_sel()
        if ch_sel:
            data = rx_data() # Receive sensor data
            if not data_ack:
                data = rx_data()
                if data_ack:
                    fault = RxFault() # Listen for previous fault data
                    #update csv files
                if rfm9x.destination == 1:
                    data_store(data, 'node1.csv')
                    if len(fault) != 0:
                        data_store(fault,'node1.csv')
                    node1 = True
                elif rfm9x.destination == 2:
                    data_store(data, 'node2.csv')
                    if len(fault) != 0:
                        data_store(fault,'node2.csv')
                    node2 = True
            else:
                fault = RxFault() # Listen for previous fault data
                #update csv files
                if rfm9x.destination == 1:
                    data_store(data, 'node1.csv')
                    if len(fault) != 0:
                        data_store(fault,'node1.csv')
                    node1 = True
                elif rfm9x.destination == 2:
                    data_store(data, 'node2.csv')
                    if len(fault) != 0:
                        data_store(fault,'node2.csv')
                    node2 = True
                    

def main():
    global ch_sel, data_ack, temp, moist, rfm9x, node1, node2
    while True:
        Channel_Selection()
        if ch_sel and data_ack: #data received correctly
            Channel_Selection() #repeat for a second node
            if not(ch_sel and data_ack):
                Fault_log(rfm9x.destination, ch_sel, data_ack)
        else:
            Fault_log(rfm9x.destination, ch_sel, data_ack)
        
        #=====================#
        #update serverside code        
        check_values()
        #=====================#
        
        # Display the most recent values on the oled screen
        header = dashboardData()
        sensor_1 = header[0]
        sensor_2 = header[1]
              
        temp1 = float(sensor_1['Temperature'])
        moist1 = float(sensor_1['Soil Moisture'])
        temp2 = float(sensor_2['Temperature'])
        moist2 = float(sensor_2['Soil Moisture'])
        display_counter = 0
        page = 1
        while display_counter <10:
            if page == 1:
                Display(page, temp1, moist1)
                page = 2
            else:
                Display(page, temp2, moist2)
                page = 1
            time.sleep(5) # Swap pages every 5 seconds
            display_counter += 1
            

setup()
main()
