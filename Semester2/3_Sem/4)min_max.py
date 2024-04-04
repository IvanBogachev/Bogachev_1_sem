def read_graph_as_edges_w():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    return graph


def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges_w()
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1],edge[2])])
    return graph_dict

def Dijkstra_max_weight(graph, v):
    d = {}
    queue = []
    visited = []
    for key in graph.keys():
        d[key] = 0
    d[v] = 10000
    queue.append([0, v])
    while queue:
        queue.sort()
        c = queue.pop(-1)
        visited.append(c[1])
        for neigh in graph[c[1]]:
             if neigh[0] not in visited:
                if min(d[c[1]], neigh[1]) > d[neigh[0]]:
                   d[neigh[0]] = min(d[c[1]], neigh[1])

                queue.append(neigh[::-1])
    return d
graph = read_graph_as_neigh_list_w()

print(Dijkstra_max_weight(graph, 1))

'''9
1 2 5
1 3 1
2 5 3
3 5 6
3 4 3
4 7 5
3 7 2
5 6 1
7 6 4'''