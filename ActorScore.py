import csv

fop = {}


def addToList(key, value):
    global fop
    if key[0] == "a":
        if key not in fop.keys():
            fop[key] = {"films": 0, "actors": 0}
    else:
        return
    if value[0] == 'f':
        fop[key]["films"] += 1
    else:
        fop[key]["actors"] += 1


file = open("edges.csv", "r", newline="")
reader = csv.reader(file)
next(reader)
for row in reader:
    addToList(row[0], row[1])
    addToList(row[1], row[0])
file.close()

valid = []
for i in fop.items():
    valid.append([i[0][2:], i[1]["films"], i[1]["actors"]])

data = open("stats.csv", "w", newline="")
writer = csv.writer(data)
writer.writerow(["actor", "films_cnt", "actors_cnt"])
writer.writerows(sorted(valid))
data.close()
