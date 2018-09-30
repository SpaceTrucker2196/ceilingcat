import time
import datetime
import logging
import serial
from terminaltables import DoubleTable
from sense_hat import SenseHat

import terminaltables

from os import system 

sense = SenseHat()
geiger = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
red = (255, 0, 0)
blue = (0, 0, 255)

logging.basicConfig(filename='sensor.log',level=logging.DEBUG)
degree_sign=chr(176) 
sense.set_imu_config(True,True,True)

while True:
    temp = sense.get_temperature()
    tempHumid = sense.get_temperature_from_humidity()
    tempPressure = sense.get_temperature_from_pressure()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    gyro = sense.get_gyroscope()
    gyroRaw = sense.get_gyroscope_raw()
    rawMag = sense.get_compass_raw()
    timestamp = time.ctime()
    accel_only = sense.get_accelerometer()
    north = sense.get_compass()

    tempLabel =  "%s C" % (temp)
    humidLabel = "Humidity: %s %%rH" % (humidity)
  
    pressureLabel = "Pressure: %s Millibars" % (pressure)
    northLabel = "North: %s" % (north)
    magLabel = "Magnetometer x: {x}, y: {y}, z: {z}".format(**rawMag)
    gyroLabel = "Gyro: p: {pitch}, r: {roll}, y: {yaw}".format(**gyro)
    accelLabel = "Accel: p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only)
    
    tempHumidLabel = "%s" % (tempHumid)
    tempPressureLabel = "%s" % (tempPressure)

    radiationBytes = geiger.read(2)
    radiationCPS = int.from_bytes(radiationBytes, byteorder='little',signed=False)

    ENVIRO = (
            ('Temp Sensor','Humidity Sensor','Pressure Sensor'),
            ('{:+3.1f} C'.format(temp),'{:+3.1f} C'.format(tempHumid),'{:+3.1f} C'.format(tempPressure)),
            (' ','Humidty: {:3.1f}%'.format(humidity),'Barimetric: {:3.3f} mb'.format(pressure)),
            )
    RAD   =  (
            ('Radiation', 'CPS:{:08d} '.format(radiationCPS),'uSv/hr'),
            )
    MAGNETIC = (
            ('To North: {:+3.1f}'.format(north),'X','Y','Z'),
            ('Field Intensity','{:+3.2f} uT'.format(rawMag['x']),'{:+3.2f} uT'.format(rawMag['y']),'{:+3.2f} uT'.format(rawMag['z'])),
            )

    GRAVITY = (
            ('','X','Y','Z'),
            ('Gyro','{:+3.2f} deg'.format(gyro['pitch']),'{:+3.2f} deg'.format(gyro['roll']),'{:+3.2f} deg'.format(gyro['yaw'])),
            ('','{:+3.2f} rad'.format(gyroRaw['x']),'{:+3.2f} rad'.format(gyroRaw['y']),'{:+3.2f} rad'.format(gyroRaw['z']))

            )

    environmentTable = DoubleTable(ENVIRO,'[ENVIRONMENTAL]' )
    environmentTable.justify_columns[2] = 'right'

    radiationTable = DoubleTable (RAD,'[IONIZING RADIATION]')

    magneticTable = DoubleTable(MAGNETIC,'[MAGNETIC FIELD]')
    magneticTable.justify_columns[1,2,3,4] = 'right'
    
    gravityTable = DoubleTable(GRAVITY,'[GYRO]')
    gravityTable.justify_columns[1,2,3,4] = 'center'
    
    
    system('clear')
    print(environmentTable.table)
    print(radiationTable.table)
    print(magneticTable.table)
    print(gravityTable.table)
   
    
    #log_record = "%s : temp=%s humidity=%s pressure=%s gyro=%s accel=%s mag=%s" % (timestamp,temp,humidity,pressure,sense.gyro,sense.accel,sense.compass_raw)
    #logging.info(log_record)
            
    #time.sleep(10)
O
