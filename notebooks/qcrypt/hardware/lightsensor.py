# standard libraries:
import time
import logging
import serial

# third party:
import paho.mqtt.client as mqtt

try:
    import RPi.GPIO as GPIO

    HARDWARE_IMPORTS = True
except ModuleNotFoundError as exception:
    print(f"{type(exception).__name__}: {exception}")
    HARDWARE_IMPORTS = False
    
class Lightsensor:
    logger = logging.getLogger("__Lightsensor__")
    formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
    streamhandler = logging.StreamHandler()
    filehandler = logging.FileHandler(filename="lightsensor.log", mode="a")
    streamhandler.setFormatter(formatter)
    filehandler.setFormatter(formatter)
    logger.addHandler(streamhandler)
    logger.addHandler(filehandler)
    
    def __init__(self,
           device="/dev/ttyACM0",
           #mqtt_broker_ip="localhost",
           log_level="INFO",
           baud_rate=9600,
           timeout=1
          ):
        self.device = device
        #self.mqtt_broker_ip = mqtt_broker_ip
        self.log_level = log_level
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.logger.setLevel(log_level)  
        self.ser = self.getSerialConnection()
        
    def getSerialConnection(self): 
        try:
            print("establishing connection to lightsensor ..")
            return serial.Serial(self.device, self.baud_rate, timeout=self.timeout)
        except serial.SerialException:
            self.logger.error("Connection could not be established")
       
    def getValues(self):
        if ser.in_waiting > 0:
            return self.ser.readline().decode("utf-8").rstrip()
            

   
    
    
 


        