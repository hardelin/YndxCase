import csv
import json

import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

file = open("stats.csv", "r", newline="")
reader = csv.reader(file)
next(reader)
data = []
actors = set()
for row in reader:
    data.append([row[0], int(row[1]), int(row[2])])
data = sorted(data, key=lambda x: -x[1])
for i in range(2):
    actors.add(data[i][0])
data = sorted(data, key=lambda x: -x[2])
for i in range(2):
    actors.add(data[i][0])
actors = list(actors)
file.close()

rows = open("graph.json", "r")
data = json.load(rows)
nodes = set()
edges = []
addis = []
for act in actors:
    nodes.add("a_"+act)
    for k in data["a_"+act]:
        nodes.add(k)
nodes = list(nodes)

goyda = open("edges.csv", "r", newline="")
redis = csv.reader(goyda)
next(redis)
for row in redis:
    if row[0] in nodes and row[1] in nodes:
        edges.append(row)

red_colors = []
blue_colors = []
i = 0
for node in nodes:
    if node[0] == 'f':
        graph.add_node(node[2:])
        red_colors.append(node[2:])
    else:
        graph.add_node(node[2:])
        blue_colors.append(node[2:])
    i += 1
for edge in edges:
    graph.add_edge(edge[0][2:], edge[1][2:])
    graph.add_edge(edge[1][2:], edge[0][2:])

plt.figure()
pos2 = nx.spring_layout(graph, seed=25, k=0.3)
nx.draw(graph,
        pos2,
        with_labels=False,
        node_size=0,
        node_color='none',
        edge_color='black',
        width=0.1,
        font_size=8
        )
for node, (x, y) in pos2.items():
    if node in red_colors:
        plt.text(x, y, node,
                 fontsize=8,
                 color="red",
                 ha='center',
                 va='center')
    else:
        plt.text(x, y, node,
                 fontsize=8,
                 color="darkblue",
                 ha='center',
                 va='center')

plt.show()

