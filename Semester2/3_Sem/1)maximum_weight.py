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
        d[key] = 100000
    d[v] = 0
    queue.append([0, v])
    while queue:
        queue.sort()
        c = queue.pop(0)
        visited.append(c[1])
        for neigh in graph[c[1]]:
             if neigh[0] not in visited:
                if max(d[c[1]], neigh[1]) < d[neigh[0]]:
                   d[neigh[0]] = max(d[c[1]], neigh[1])

                queue.append(neigh[::-1])
    return d
graph = read_graph_as_neigh_list_w()

print(Dijkstra_max_weight(graph, 1))
'''9
1 2 5
1 3 1
2 5 1
3 5 6
3 4 3
4 7 5
3 7 2
5 6 1
7 6 4'''

'''10
1 2 1
2 4 8
4 6 3
6 8 2
8 10 4
1 3 10
3 5 11
5 7 22
7 9 5
9 10 4
'''
