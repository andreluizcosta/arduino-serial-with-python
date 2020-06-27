import serial

ser = serial.Serial('COM3', baudrate=9600, timeout=1)
a=0

while a==0:
    arduinoData = ser.readline()
    print(arduinoData)

    if b'1' in arduinoData:
        print('a')
        a = 1
