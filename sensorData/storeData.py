import sqlite3
import datetime
import random
import time

conn = sqlite3.connect('tomatoData.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS readings(datestamp TEXT, sensor TEXT, value REAL)')

def data_entry(sensor,value):
    datestamp = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO readings(datestamp,sensor,value) VALUES (?,?,?)",(datestamp,sensor,value))
    conn.commit()

if __name__ == "__main__":
    try:
        create_table()
        while True:
            light = random.randrange(0,100)
            moist = random.randrange(0,100)
            airTemp = random.randrange(0,100)
            soilTemp = random.randrange(0,100)
            humid = random.randrange(0,100)
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
    except:
        c.close()
        conn.close()
