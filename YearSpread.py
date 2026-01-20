import csv

file = open("imdb_top_1000.csv", "r", newline="")
reader = csv.reader(file)
k = {}
next(reader)
for row in reader:
    if row[2].isdigit():
        if row[2] in k.keys():
            k[row[2]] += 1
        else:
            k[row[2]] = 1
file.close()
res = open("spri.csv", "w", newline="")
writer = csv.writer(res)
data = []
for i in k.items():
    data.append([int(i[0]), i[1]])
writer.writerow(["date", "count"])
writer.writerows(sorted(data))
res.close()
