import math
import time
import tkinter
import serial
from random import random
from serial import Serial
 
 # set the serial port for reading from the microcontroller
ser = serial.Serial("COM3", 9600)

# reset and send commands to the board in ASCII
# print("sending to board")
print("waiting for data")
ser.write(bytearray('\x03','ascii')) # ascii code for ctrl+c
ser.write(bytearray('\x02','ascii')) # ctrl+b
ser.write(bytearray('\x04','ascii')) # ctrl+d
print("sending to board")

# create our variables for printing 
array =[]	# create an array to store the data
cont = 1	# variable for running the read function
time=[]	 	# list to store our time values
pos=[]	# list to store our volt values
start=0 #boolean to show start of step response data
# while cont is true read values from the serial port
while cont == 1:
    #print('looping!')
    value = ser.readline().decode('utf-8').strip()
    if value == 'awaiting input':
        number = 1
        ser.write(bytes(str(number).encode('utf-8')))
        ser.write(bytearray('\x0D','ascii'))
    print(value)
    if value == 'start':
        start=1
        print("reading!")
    while start==1:
        value = ser.readline().decode('utf-8').strip()
        print(value)
        if value == 'end':	# once end is printed by the microcontroller stop reading values
            
            start = 0
            cont=0
        else:
            array.append(value)	# append values to out array
