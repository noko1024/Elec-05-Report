import csv
import sys
import datetime
import matplotlib.pyplot as plt

source = {
    "Mon": [],
    "Tue": [],
    "Wed": [],
    "Thu": [],
    "Fri": [],
    "Sat": [],
    "Sun": []
}

with open('./tepco2023_4.csv') as csvfile:
    reader = csv.reader(csvfile)
    target_week = ""
    for row in reader:
        day = datetime.datetime.strptime(row[0], '%Y/%m/%d')
        week = day.strftime('%a')

        if week != target_week:
            target_week = week
            data = source[week]
            data.append([])
            source[week] = data

        data = source[week]
        data[-1].append([day, row[2]])
        source[week] = data



plt.legend()
plt.grid()
plt.show()

fig = plt.figure()

fig.legend()
