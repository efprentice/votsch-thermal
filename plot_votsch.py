# -*- coding: utf-8 -*-
"""
This script plots auto-generated csv files from arduino_readtemp-press-humid.py
It is intended to create a timeseries of temperature, pressure, and humidity
inside the Votsch 4011 thermal chamber at NTNU via the BME280 sensor connected
to an Arduino Uno.

Created on Thu Jan 21 14:16:49 2021
Updated on Thu Jul 08 09:18:00 2021

@author: elizabep
"""


import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


###################### GLOBAL PARAMETERS ######################

folder = 'csv/'
file = 'test2.csv'

#################### SCRIPT ####################

plt.close()

df = pd.read_csv(folder+file)
df['Time'] = df['Time'].map(lambda x:dt.datetime.strptime(str(x),'%H:%M:%S'))


fig,[ax1,ax2,ax3] = plt.subplots(3,sharex=True)

ax1.set_title('Votsch Thermal Chamber: Sensor Readings')
ax1.plot(df['Time'],df['Temp[C]'],'tab:blue')
ax1.set_ylabel('Temperature [degC]')

ax2.plot(df['Time'],df['Humidity[%]'],'tab:orange')
ax2.set_ylabel('Humidity [%]')

ax3.plot(df['Time'],df['Pressure[mb]'],'tab:green')
ax3.set_ylabel('Pressure [mb]')
plt.ticklabel_format(axis='y',useOffset=False)
ax3.set_xlabel('Time')

plt.show()

fig.savefig('plots/fig1_votsch.png')
