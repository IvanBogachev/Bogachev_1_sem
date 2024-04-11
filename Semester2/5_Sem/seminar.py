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



def kruskal(graph): # read_graph_as_edges
    g = graph
    for v in g:
        v[0],v[2] = v[2], v[0]
    g.sort()

    tree_v = set()
    tree_e = []

    for e in g:
        if e[1] not in tree_v or e[2] not in tree_v:
            tree_v.add(e[1])
            tree_v.add(e[2])
            tree_e.append(e)
        else:
            continue
    return tree_e


from heapq import *


def prim(graph):  # read_graph_as_neigh_list_w

    v = 1
    tmp = list(graph[v])
    h = []

    for e in tmp:
        h.append([e[1], e[0], v])
    heapify(h)
    tree_v = set()
    tree_e = []

    while h:
        e_min = heappop(h)
        if e_min[1] not in tree_v:
            tree_v.add(e_min[1])
            for e in graph[e_min[1]]:
                t = [e[1], e[0]]
                heappush(h, (list(t) + [e_min[1]]))
            v = e_min[1]
            tree_e.append(e_min)

        else:
            continue

    return tree_e



graph =  read_graph_as_neigh_list_w()

print(prim(graph))