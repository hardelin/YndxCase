import csv
import json
rows = open("gra.json", "r")
data = json.load(rows)
print(data)