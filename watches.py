import time
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

    print("Temperature: %s C" % temp)
    print("Humidity: %s %%rH" % humidity)
    print("Pressure: %s Millibars" % pressure)
    print("Magnetometer x: {x}, y: {y}, z: {z}".format(**rawMag))
    print("Orientation: p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

    pixels = [red if i < temp else blue for i in range(64)]

    sense.set_pixels(pixels)

    time.sleep(60)

