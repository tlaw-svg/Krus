from functools import cmp_to_key
import time



locations = {}


def location_id(name):
    if name not in locations:
        locations[name] = len(locations)
    return locations[name]


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
with open("input1.txt", "r") as myfile:
    for line in myfile:
        line = line.strip()
        if not line:
            continue
        src, dst, w = line.split(",")
        u = location_id(src)
        v = location_id(dst)
        w = int(w)
        edges.append([u, v, w])

V = len(locations)
id_to_name = {i: name for name, i in locations.items()}

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

start_time = time.perf_counter()
MST_cost, MST_edges = Kruskals_mst()
end_time = time.perf_counter()


print("MST Costs:", MST_cost)
print("Edges in MST:")
for x,y,z in MST_edges:
    print(f"{id_to_name[x]} <-----> {id_to_name[y]} weight: {z}")


print(f"Execution Time: {end_time - start_time:.4f} seconds")