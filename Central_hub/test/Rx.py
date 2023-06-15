import board, busio, digitalio
import adafruit_rfm9x
import time

#Initialize the LoRa module
def rfm_initialize():
    global rfm9x
    #Initialize the GPIO connections
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs =digitalio.DigitalInOut(board.CE1)
    reset = digitalio.DigitalInOut(board.D25)
    g0 = digitalio.DigitalInOut(board.D24)

    #Set up the rfm9x object module
    while True:
        try:
            rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
            print('RFM9x: Detected')
            break
        except RuntimeError as error:
            print('RFM9x Error: ', error)
            time.sleep(3)

    #Enable CRC Checking
    rfm9x.enable_crc = True
    # Set node address - Central hub
    rfm9x.node = 0

    return rfm9x

#Channel selection
def channel_sel():
    global ch_sel, rfm9x
    ch_sel = False
    print('Listening for Request')
    channel_req_byte = rfm9x.receive(timeout=35.0)
    print(channel_req_byte)
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
    #return ch_sel

#Receive packet from sensor node
def rx_data():   
    print('Listening for data...')
    sens_data_byte = rfm9x.receive(timeout=10.0)
    if sens_data_byte is not None:
        rfm9x.send("Data ACK".encode('utf-8')) # send ACK
        sens_data = sens_data_byte.decode('utf-8')
        print('Received: {0}'.format(sens_data))
        return sens_data
    else:
        print('Data NOT recieved')

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

#Sleep function
def Rfm9x_sleep(sleep_time):
    rfm9x.sleep()
    time.sleep(sleep_time)
    rfm9x.sleep()
    
# Storage file selection function
def sel_file():
    if rfm9x.destination == 1:
        filename = 'node1.csv'
    elif rfm9x.destination == 2:
        filename = 'node2.csv'
    else:
        filename = 'error.csv'
    return filename
