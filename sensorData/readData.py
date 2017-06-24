import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tomatoData.db')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM readings')
    data = c.fetchall()
    for row in data:
        print(row)

read_from_db()

c.close
conn.close()