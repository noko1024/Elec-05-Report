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
        data[-1].append([day, int(row[2])])
        source[week] = data

plot_data = []
plot_label = []

for idx, row in enumerate(source['Sun']):
    data = [list(x) for x in zip(*row)]
    label = data[0][0].strftime('%Y/%m/%d')
    plt.plot(range(len(data[1])), data[1], label=label)


plt.ylabel('power Consumption (1000kWh)')

plt.grid()
plt.show()
