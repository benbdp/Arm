import mysql.connector
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from dateutil import parser
# from matplotlib import style
# style.use('fivethirtyeight')

conn = mysql.connector.connect(user='root',password='password',host='tomatoarm.cwg4p0agnguy.us-east-2.rds.amazonaws.com',database='tomato_data')
c = conn.cursor()

def read_from_db():
    c.execute("SELECT * FROM humidity")
    data = c.fetchall()
    for row in data:
        print(row)

def compute_mean():
    c.execute("SELECT * FROM readings WHERE sensor = 'moist'")
    data = c.fetchall()
    vals = []
    for row in data:
        vals.append(row[2])
    mean = (sum(vals)) / (len(vals))
    print("mean: ", mean)

    sort = sorted(vals)
    print(sort)
    length = len(sort)
    print("len: ",length)
    side = (length/2)
    if side.is_integer() == False:
        med = int(side)
        print("median: ",sort[med])

        median = sort[med]
        return mean, median


    elif side.is_integer() == True:
        pos1 = int(side-0.5)
        pos2 = int(side+0.5)
        mid = sort[pos1] + sort[pos2]

        median = mid/2

        print("median: " ,median)
        return mean, median


def graph_data():
    c.execute("SELECT datestamp, value FROM readings WHERE sensor = 'moist"
              "'")
    data = c.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.axhline(y=compute_mean()[0], color='r', linestyle='-')  # mean
    plt.axhline(y=compute_mean()[1], color='g', linestyle='-')  # median
    plt.show()

# read_from_db()
# graph_data()

read_from_db()

c.close
conn.close()