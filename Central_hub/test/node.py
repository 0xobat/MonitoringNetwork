import board, busio, digitalio
import adafruit_rfm9x
import time, json
from adafruit_seesaw.seesaw import Seesaw

channel_ack = False
data_ack = False
sens_data = 0
fault_log = []

###Initialize pins and objects
def setup():
    global ss, rfm9x
    #Soil sensor pins
    i2c = busio.I2C(scl=board.GP1, sda=board.GP0)  # uses board.SCL and board.SDA
    #RFM95 pins
    spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)
    cs =digitalio.DigitalInOut(board.GP17)
    reset = digitalio.DigitalInOut(board.GP20)
    g0 = digitalio.DigitalInOut(board.GP7)

    ###Initialize objects
    ss = Seesaw(i2c, addr=0x36)
    rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
    #Initialize rfm9x parameters
    rfm9x.enable_crc = True #Enable CRC Checking
    rfm9x.node = 1   # Node address
    rfm9x.destination = 0    #Destination address

#Read moisture and temperature levels
def read_sens():
    global sens_data
    moist = ss.moisture_read()
    temp = ss.get_temp()
    data = [ {'Time': int(time.time()), 'Temperature': temp, 'Soil Moisture': moist} ]
    sens_data = bytearray(json.dumps(data).encode('utf-8'))
    #return sens_data

#Channel request
def Channel_req():
    global channel_ack
    channel_ack = False
    rfm9x.send('1 Channel request'.encode('utf-8'))     #send request to Hub
    channel_ack_byte = rfm9x.receive(timeout=10.0)      #listen for approval message
    if channel_ack_byte is not None:
        channel_ack = True      #channel_ack_byte.decode('utf-8')
        #print('Received: {0}'.format(channel_ack))
    else:
        channel_ack = False
        print('Channel Request Failure')
    #return channel_ack

#Send data to central hub
def tx_data(channel_ack, sens_data):
    global data_ack
    data_ack = False
    if channel_ack:
        rfm9x.send(sens_data)       #send data
        #Listen for ACK
        ACK_data_byte = rfm9x.receive(timeout=5.0)
        if ACK_data_byte is not None:
            ACK_data = ACK_data_byte.decode('utf-8')
            print('Received: {0}'.format(ACK_data))
            data_ack = True
        else:
            print('Data ACK failure')
            data_ack = False
    #return data_ack

# Fault Handling
def Fault_log(channel_ack, data_ack, sens_data):
    global fault_log
    if channel_ack or data_ack  is False:
        fault_log.append(sens_data)
    else:
        rfm9x.send(fault_log)       #send the fault log
        #Listen for ACK
        Fault_ACK_byte = rfm9x.receive(timeout=5.0)
        if Fault_ACK_byte is not None:
            Fault_ACK = Fault_ACK_byte.decode('utf-8')
            print('Fault Log Transmitted Received : {0}'.format(Fault_ACK))
            fault_log = {}
        else:
            print('Fault log Transmission FAILURE')
            
#RFM9x Sleep function
def RFM9x_sleep(sleep_time):
    rfm9x.sleep()
    time.sleep(sleep_time)
    rfm9x.sleep()


# Main code to run indefinetely
def main():
    global sens_data, channel_ack, data_ack
    while True:
        read_sens() # Read sensor values
        Channel_req() # Request central hub channel
        if channel_ack:
            # Transmit sensor data to central hub
            tx_data(channel_ack, sens_data)
            if not data_ack: # retry data transmission on ACK Failure
                for retry in range(1,3):
                    tx_data(channel_ack, sens_data)
                    if data_ack:
                        break  # exit the loop if data_ack is True
        else: # retry channel request on ACK Failure
            for retry in range(1,4):
                Channel_req()
                if channel_ack:
                    tx_data(channel_ack, sens_data)
                    if not data_ack: # retry data transmission on ACK Failure
                        for retry in range(1,4):
                            tx_data(channel_ack, sens_data)
                            if data_ack:
                                break  # exit the loop if data_ack is True
                    break  # exit the loop if channel_ack is True
                time.sleep(5)    # delay 5s before next channel request  retry
        
        #add to fault log
        Fault_log(channel_ack, data_ack, sens_data)
        #sleep till next read
        RFM9x_sleep(30)	#30 seconds
    
setup()
main()