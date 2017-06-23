import sqlite3
import datetime

conn = sqlite3.connect('tomatoData.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS readings(datestamp TEXT, sensor TEXT, value REAL)')

def data_entry():
    datestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO readings(datestamp,sensor,value) VALUES (?,?,?)",(datestamp,sensor,value))
    conn.commit()




c.close()
conn.close()