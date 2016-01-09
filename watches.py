import time
import datetime
from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    gyro = sense.get_gyroscope()
    rawMag = sense.get_compass_raw()
    timestamp = time.ctime()
    accel_only = sense.get_accelerometer()
    north = sense.get_compass()

    print("____________________________________________________________________")
    print("Temperature: %s C" % temp)
    print("Humidity: %s %%rH" % humidity)
  
    print("Pressure: %s Millibars" % pressure)
    print("North: %s" % north)
    print("Magnetometer x: {x}, y: {y}, z: {z}".format(**rawMag))
    print("Gyro: p: {pitch}, r: {roll}, y: {yaw}".format(**gyro))
    print("Accel: p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))
    
    log_record = "%s : temp=%s humidity=%s pressure=%s gyro=%s accel=%s mag=%s" % (timestamp,temp,humidity,pressure,sense.gyro,sense.accel,sense.compass_raw)
    print(log_record)
    
    pixels = [red if i < temp else blue for i in range(64)]

    sense.set_pixels(pixels)

    time.sleep(10)

