def read_graph_as_edges_w():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges_w()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1],edge[2])])
    return graph_dict

def Bellman_Ford(graph, s):
    d = {}
    for key in graph.keys():
        d[key] = 1000
    d[s] = 0
    n = len(d)
    for j in range(n - 1):
        for i in graph:
            for neigh in graph[i]:
                u = i
                v = neigh[0]
                w = neigh[1]
                if d[v] > (d[u] + w):
                    d[v] = (d[u] + w)
    return d

graph = read_graph_as_neigh_list_w()

print(Bellman_Ford(graph, 1))
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


