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
    orientation = sense.get_orientation_degrees()
    rawMag = sense.get_compass_raw()
    timestamp = time.ctime()

    print("____________________________________________________________________")
    print("Temperature: %s C" % temp)
    print("Humidity: %s %%rH" % humidity)
    print("Pressure: %s Millibars" % pressure)
    print("Magnetometer x: {x}, y: {y}, z: {z}".format(**rawMag))
    print("Orientation: p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
    
    log_record = "%s temp=%s humidity=%s pressure=%s" % (timestamp,temp,humidity,pressure)
    print(log_record)
    
    pixels = [red if i < temp else blue for i in range(64)]

    sense.set_pixels(pixels)

    time.sleep(10)

