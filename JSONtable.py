import json
import csv

data = {}


def addToJson(key, value):
    global data
    if key not in data:
        data[key] = [value]
    else:
        data[key].append(value)


file = open("edges.csv", "r", newline="")
reader = csv.reader(file)
next(reader)

for row in reader:
    addToJson(row[0], row[1])
    addToJson(row[1], row[0])
file.close()

file = open("gra.json", "w")
json.dump(data, file)
file.close()
