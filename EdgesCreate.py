# Poster_Link, 0
# Series_Title, 1
# Released_Year, 2
# Certificate, 3
# Runtime, 4
# Genre, 5
# IMDB_Rating, 6
# Overview, 7
# Meta_score, 8
# Director, 9
# Star1, 10
# Star2, 11
# Star3, 12
# Star4, 13
# No_of_Votes,
# Gross

import csv

edges = set()


def addMovieAndActor(row):
    global edges
    for i in range(1, len(row)):
        edges.add(tuple([f"f_{row[0]}", f"a_{row[i]}"]))
    return


def addActorAndActor(row):
    global edges
    tmp = sorted(row[1:])
    for i in range(0, len(tmp)):
        for j in range(i + 1, len(tmp)):
            edges.add(tuple([f"a_{tmp[i]}", f"a_{tmp[j]}"]))
    return


file = open("imdb_top_1000.csv", "r", newline="")
reader = csv.reader(file)
k = []
next(reader)
for row in reader:
    k.append([row[1], row[10], row[11], row[12], row[13]])
file.close()
for k_row in k:
    addMovieAndActor(k_row)
    addActorAndActor(k_row)

res = open("edges.csv", "w", newline="")
writer = csv.writer(res)
writer.writerow(["first", "second"])
writer.writerows(sorted(list(edges)))
res.close()

