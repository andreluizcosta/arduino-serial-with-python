import serial
import time

# First, you need to define the serial port and the serial communication rate.
# Make sure that the 'COM#' corresponds to what was seen in the Windows Device Manager.
ser = serial.Serial('COM3', 9600)

def blink_led():
    #According to what the users write, the program will send a letter through the arduino's serial communication
    user_input = input("\n Type on, off or quit : ")

    if user_input =="on":
        print("Turning on the LED")
        time.sleep(0.1)
        ser.write(b'H')
        blink_led()

    elif user_input =="off":
        print("Turning off the LED")
        time.sleep(0.1)
        ser.write(b'L')
        blink_led()

    elif user_input =="quit":
        #Besides exiting, the program turns off the LED and ends the serial communication
        print("Exiting")
        time.sleep(0.1)
        ser.write(b'L')
        ser.close()

    else:
        print("Invalid input. Type on / off / quit.")
        blink_led()

time.sleep(2) # wait for the serial connection to initialize

#calling the function
blink_led()
