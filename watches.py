import time
from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    print("Temperature: %s C" % temp)
    print("Humidity: %s %%rH" % humidity)
    print("Pressure: %s Millibars" % pressure)

    pixels = [red if i < temp else blue for i in range(64)]

    sense.set_pixels(pixels)

    time.sleep(60)

