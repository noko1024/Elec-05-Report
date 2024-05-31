import csv
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
        data[-1].append([day, float(row[2])])
        source[week] = data

plot_data = []
plot_label = []
for idx, row in enumerate(source['Sun']):
    data = [list(x) for x in zip(*row)]
    plot_data.append(data[1])
    plot_label.append(data[0][0].strftime('%Y/%m/%d'))


plt.hist(plot_data, stacked=False, bins=10, label=plot_label)

plt.xlabel('power Consumption (1000kWh)')
plt.ylabel("Frequency")

plt.legend()
plt.grid()
plt.show()
