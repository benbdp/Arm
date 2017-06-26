import serial,time,datetime
# initialize serial port
ser = serial.Serial('COM4', baudrate=9600, timeout=1)

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

# def getHumid():
#     ser.write(b'h')  # send "h" to arduino for humidity reading
#     humidReading = ser.readline().decode('ascii')  # read from arduino
#     humidReading = humidReading.rstrip()   # remove whitespace
#     return humidReading  # return reading

# test function to combine two functions
def getHumid():
    ser.write(b'h')  # send "h" to arduino for humidity reading
    humidReading = ser.readline().decode('ascii')  # read from arduino
    humidReading = humidReading.rstrip()   # remove whitespace
    while len(humidReading) == 0:
        ser.write(b'h')
        return humidReading

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

# function prints the data along with the timestamp associated with it
def printData(now):
    f.write("data at: " + str(now)+"\n")
    f.write("light: " + str(getLightReturn()) + "\n")
    f.write("moisture: " + str(getMoistReturn()) + "\n")
    f.write("air temperature: " + str(getAirTempReturn()) + "\n")
    f.write("soil temperature: " + str(getSoilTempReturn()) + "\n")
    f.write("humidity: " + str(getHumidReturn()) + "\r\n")




if __name__ == "__main__":
    f = open('data.txt', 'w+')
    try:
        status = True
        counter = 0
        print("starting to collect data")
        while status:
            print(counter)
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            printData(now)
            print("storing data!")
            time.sleep(5)
            counter += 1
            if counter == 20:
                print("done collecting data!")
                status = False
    except:
        f.close()
        ser.close()
