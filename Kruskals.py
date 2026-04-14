from functools import cmp_to_key
from enum import Enum

class buildings(Enum):
    Olin = 0
    Burwell = 1
    Science_Center = 2
    Main = 3
    Library = 4


def reachable(start, target, graph, visited):
    if start == target:
        return True
    visited[start] = True

    for neighbor in graph[start]:
        if not visited[neighbor]:
            if reachable(neighbor, target, graph, visited):
                return True
    return False

def compare(a, b):
    return a[2] - b[2]


edges = []
with open("input.txt", "r") as myfile:
    for line in myfile:
        line = line.strip()
        if not line:
            continue
        src, dst, w = line.split(",")
        u = buildings[src].value
        v = buildings[dst].value
        w = int(w)
        edges.append([u, v, w])

V = len(buildings)

edges = sorted(edges, key=cmp_to_key(compare))


def Kruskals_mst():
    graph = {i: [] for i in range(V)}
    MST_cost = 0
    count = 0
    MST_edges = []

    for u, v, w in edges:
        visited = [False] * V
        if reachable(u, v, graph, visited):
            continue
        graph[u].append(v)
        graph[v].append(u)
        MST_edges.append((u,v,w))
        MST_cost += w
        count += 1

        if count == V - 1:
            break

    return MST_cost, MST_edges


MST_cost, MST_edges  = Kruskals_mst()

print("MST Costs:", MST_cost)
print("Edges in MST:")
for x,y,z in MST_edges:
    print(f"{buildings(x).name} <-----> {buildings(y).name}   weight: {z}")