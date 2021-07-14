import os
import serial
import time
import io
import sys

import csv

from datetime import datetime


serial_port_name = "/dev/ttyUSB0"
baudrate = 9600
time_delay = 60 # seconds

def main():
	ser = serial.Serial(serial_port_name, baudrate, timeout=1)
	if ser.isOpen():
     		print(ser.name + ' is open')

	fname = raw_input("Give a name to the csv file: ")
	fname = fname+".csv"

	fields=['Date','Time','Temp_1']

	with open(fname, 'w') as f:
    		writer = csv.writer(f)
    		writer.writerow(fields)

	print(fields)

	while True:

		command = '$12|<CR>'
		print(command.encode())		
		ser.write(command.encode())
		temp_1 = ser.read(100)
		print(temp_1)

		#ser.write("IN_PV_00\r\n".encode())
		#temp_1 = ser.print(bmp.readTemperature())
		#outflow_temp_str = outflow_temp_str.split()

		#ser.write("IN_PV_03\r\n".encode())
		#external_temp_str = ser.read(100)
		#external_temp_str = external_temp_str.split()

		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		date = now.strftime('%D')

		fields=[date,current_time,temp_1]
		print(fields)

		with open(fname, 'a') as f:
    			writer = csv.writer(f)
    			writer.writerow(fields)

		time.sleep(time_delay)

main()
