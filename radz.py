import serial
    
ser = serial.Serial('/dev/ttyUSB0',9600,timeout=5)  # open serial port
print(ser.name)
data = ser.read(2)
count = int.from_bytes(data, byteorder='little',signed=False)
print(count)
ser.close()   
