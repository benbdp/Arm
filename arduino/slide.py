import serial,time,datetime
# initialize serial port
ser = serial.Serial('COM4', baudrate=9600, timeout=1)