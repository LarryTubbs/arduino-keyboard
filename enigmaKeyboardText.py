import serial
import time
import signal
import sys

PORT = '/dev/cu.usbmodemHIDPC1'
ser = serial.Serial(port=PORT, baudrate=9600)

def signal_handler(sig, frame):
    ser.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to cancel')

def encode(c):
    print('light lamp: ' + c)

def lamp_off():
    print('lamp off')

while True:
    c = ser.read_until().decode("utf-8")
    c = c.rstrip()
    if c == '-':
        print('lamp off')
    else:
        encode(c)
    time.sleep(0.2)