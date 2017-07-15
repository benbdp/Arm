import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.dates as md
from dateutil import parser
from matplotlib import style
import datetime as dt
import numpy as np
import dateutil

style.use('fivethirtyeight')

conn = mysql.connector.connect(user='root',password='password',host='tomatoarm.cwg4p0agnguy.us-east-2.rds.amazonaws.com',database='tomato_data')
c = conn.cursor()


def get_light():
    c.execute("SELECT * FROM light")
    data = c.fetchall()
    dates = []
    values = []
    for row in data:
        dates.append((row[0]))
        values.append(row[1])
    return dates,values


def get_moisture():
    c.execute("SELECT * FROM moisture")
    data = c.fetchall()
    dates = []
    values = []
    for row in data:
        dates.append((row[0]))
        values.append(row[1])
    return dates,values


def get_humidity():
    c.execute("SELECT * FROM humidity")
    data = c.fetchall()
    dates = []
    values = []
    for row in data:
        dates.append((row[0]))
        values.append(row[1])
    return dates,values


def get_air_temp():
    c.execute("SELECT * FROM air_temp")
    data = c.fetchall()
    dates = []
    values = []
    for row in data:
        dates.append((row[0]))
        values.append(row[1])
    return dates,values


def get_soil_temp():
    c.execute("SELECT * FROM soil_temp")
    data = c.fetchall()
    dates = []
    values = []
    for row in data:
        dates.append(str((row[0])))
        values.append(row[1])
    return dates,values,'soil_temp'


# def compute_mean():
#     c.execute("SELECT * FROM humidity")
#     data = c.fetchall()
#     vals = []
#     for row in data:
#         vals.append(row[1])
#     mean = (sum(vals)) / (len(vals))
#     print("mean: ", mean)
#
#     sort = sorted(vals)
#     print(sort)
#     length = len(sort)
#     print("len: ",length)
#     side = (length/2)
#     if side.is_integer() == False:
#         med = int(side)
#         print("median: ",sort[med])
#
#         median = sort[med]
#         return mean, median
#
#
#     elif side.is_integer() == True:
#         pos1 = int(side-0.5)
#         pos2 = int(side+0.5)
#         mid = sort[pos1] + sort[pos2]
#
#         median = mid/2
#
#         print("median: " ,median)
#         return mean, median




def graph_data(data):
    dates = data[0]
    values = data[1]

    dates = [dateutil.parser.parse(s) for s in dates]
    ax = plt.gca()
    ax.set_xticks(dates)

    print(dates)

    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)

    plt.plot(dates, values, "-")

    plt.xlabel('Dates')
    plt.ylabel('Values')
    plt.title(data[2])
    plt.show()

    plt.show()

# read_from_db()
# graph_data()

graph_data(get_soil_temp())
c.close
conn.close()