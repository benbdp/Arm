import sqlite3
import datetime
import random
import time
import serial
# initialize serial port
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

conn = sqlite3.connect('tomatoData.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS readings(datestamp TEXT, sensor TEXT, value REAL)')

def data_entry(sensor,value):
    datestamp = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO readings(datestamp,sensor,value) VALUES (?,?,?)",(datestamp,sensor,value))
    conn.commit()


# functions that request and read data from the arduino
def getLight():
    ser.write(b'l')  # send "l" to arduino for light reading
    lightReading = ser.readline().decode('ascii')
    lightReading = lightReading.rstrip()  # remove whitespace
    return lightReading  # return reading

def getMoist():
    ser.write(b'm')  # send "m" to arduino for soil moisture
    moistReading = ser.readline().decode('ascii')  # read from arduino
    moistReading = moistReading.rstrip()   # remove whitespace
    return moistReading  # return reading

def getAirTemp():
    ser.write(b'a')  # send "a" to arduino for air temperature reading
    tempReading = ser.readline().decode('ascii')  # read from arduino
    tempReading = tempReading.rstrip()   # remove whitespace
    return tempReading  # return reading

def getSoilTemp():
    ser.write(b's')  # send "s" to arduino for soil temperature reading
    tempReading = ser.readline().decode('ascii')  # read from arduino
    tempReading = tempReading.rstrip()   # remove whitespace
    return tempReading  # return reading

def getHumid():
    ser.write(b'h')  # send "h" to arduino for humidity reading
    humidReading = ser.readline().decode('ascii')  # read from arduino
    humidReading = humidReading.rstrip()   # remove whitespace
    return humidReading  # return reading

# functions that make sure that we actually have received data
def getLightReturn():
    while len(getLight()) == 0:
        getLight()
    return getLight()

def getMoistReturn():
    while len(getMoist()) == 0:
        getMoist()
    return getMoist()

def getAirTempReturn():
    while len(getAirTemp()) == 0:
        getAirTemp()
    return getAirTemp()

def getSoilTempReturn():
    while len(getSoilTemp()) == 0:
        getSoilTemp()
    return getSoilTemp()

def getHumidReturn():
    while len(getHumid()) == 0:
        getHumid()
    return getHumid()

if __name__ == "__main__":
    try:
        print("created db")
        create_table()
        num = 1000
        for i in range(num):
            print("reading: ",i)
            light = getLightReturn()
            moist = getMoistReturn()
            airTemp = getAirTempReturn()
            soilTemp = getSoilTempReturn()
            humid = getHumidReturn()
            readings =[light,moist,airTemp,soilTemp,humid]
            for index, item in enumerate(readings):
                if index == 0:
                    data_entry("light", item)
                if index == 1:
                    data_entry("moist", item)
                if index == 2:
                    data_entry("airTemp", item)
                if index == 3:
                    data_entry("soilTemp", item)
                if index == 4:
                    data_entry("humid", item)


            time.sleep(1)
        print("done readings")
    except:
        c.close()
        conn.close()
