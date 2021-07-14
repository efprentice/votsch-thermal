import os
import serial
import time
import io
import sys

import csv

from datetime import datetime


serial_port_name = '/dev/ttyACM0'
baudrate = 9600
time_delay = 2 # seconds

def main():
	ser = serial.Serial(serial_port_name, baudrate, timeout=1)
	if ser.isOpen():
     		print(ser.name + ' is open')

	fname = raw_input('Give a name to the csv file (eg YYYYMMDD_model-description): ')
	fname = fname+'.csv'

	fields=['Date','Time','Pressure[mb]','Humidity[%]','Temp[C]']

	with open(fname, 'w') as f:
    		writer = csv.writer(f)
    		writer.writerow(fields)

	print(fields)

	while True:

		readout = ser.read(100)
		readout_list = readout.split()

		press = readout_list[0]
		humid = readout_list[2]
		tempc = readout_list[4]

		now = datetime.now()
		current_time = now.strftime('%H:%M:%S')
		date = now.strftime('%D')

		fields=[date,current_time,press,humid,tempc]
		print(fields)

		with open(fname, 'a') as f:
    			writer = csv.writer(f)
    			writer.writerow(fields)

		time.sleep(time_delay)

main()
