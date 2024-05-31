import csv
import sys
import datetime


source = {
    "Mon": [],
    "Tue": [],
    "Wed": [],
    "Thu": [],
    "Fri": [],
    "Sat": [],
    "Sun": []
}

with open("./tepco2023_4.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        tdatatime = datetime.datetime.strptime(
            row[0]+","+row[1], '%Y/%m/%d,%H:%M')
        week = tdatatime.strftime("%a")
        day = datetime.date(tdatatime.year, tdatatime.month, tdatatime.day)

        data = source[week]
        data.append([day, row[2]])
        source[week] = data


m1 = source.get("Mon")[0:24]
m2 = source.get("Mon")[25:49]
m3 = source.get("Mon")[50:74]
m4 = source.get("Mon")[75:99]

print(source.get("Mon")[0])

# pit.plot(x,result.T[0],marker="^",label="1")
# pit.plot(x,result.T[1],marker="v",label="2")
# pit.plot(x,result.T[2],marker="D",label="3")
# pit.plot(x,avarage,marker=".",label="avarage")
#
# pit.title("Positive Electrode")
# pit.ylabel("Spark Voltage (kV)")
# pit.xlabel("Gap Length (cm)")
#
# pit.legend()
# pit.grid(True)
#
# plt.figure()
#
# pit.show()
