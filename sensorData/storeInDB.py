import mysql.connector
import serial
import time
# initialize serial port
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)


conn = mysql.connector.connect(user='root',password='password',host='tomatoarm.cwg4p0agnguy.us-east-2.rds.amazonaws.com',database='tomato_data')
c = conn.cursor()

def light_entry(value):
    timestamp = int(time.time())
    # print(timestamp)
    c.execute("INSERT INTO light(timestamp,value) VALUES (%s,%s)",(timestamp,value))
    conn.commit()

def air_temp_entry(value):
    timestamp = int(time.time())
    # print(timestamp)
    c.execute("INSERT INTO air_temp(timestamp,value) VALUES (%s,%s)",(timestamp,value))
    conn.commit()
def moisture_entry(value):
    timestamp = int(time.time())
    # print(timestamp)
    c.execute("INSERT INTO moisture(timestamp,value) VALUES (%s,%s)",(timestamp,value))
    conn.commit()

def soil_temp_entry(value):
    timestamp = int(time.time())
    # print(timestamp)
    c.execute("INSERT INTO soil_temp(timestamp,value) VALUES (%s,%s)",(timestamp,value))
    conn.commit()

def humidity_entry(value):
    timestamp = int(time.time())
    # print(timestamp)
    c.execute("INSERT INTO humidity(timestamp,value) VALUES (%s,%s)",(timestamp,value))
    conn.commit()

#######################################################################################################

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

#############################################################################################################

if __name__ == "__main__":
    try:
        num_of_readings = 480
        for i in range(num_of_readings):
            print(i)
            light = getLightReturn()
            light_entry(light)

            moist = getMoistReturn()
            moisture_entry(moist)

            airTemp = getAirTempReturn()
            air_temp_entry(airTemp)

            soilTemp = getSoilTempReturn()
            soil_temp_entry(soilTemp)

            humid = getHumidReturn()
            humidity_entry(humid)

            time.sleep(60)
    except:
        c.close()
        conn.close()
