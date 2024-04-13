def read_graph_as_edges_1():
    n = int(input())
    graph = [list(map(str, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_edges_2():
    gp = read_graph_as_edges_1()
    graph = []
    for i in range(len(gp)):
        if gp[i][0] == "<":
            graph.append([int(gp[i][1]),int(gp[i][2]),int(gp[i][3])])
        else:
            graph.append([int(gp[i][2]), int(gp[i][1]), (-1)*int(gp[i][3])])
    return graph

def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges_2()
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

def Bellman_Ford_yes_or_not_negative_cycle(graph, s):
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

    for i in graph:
        for neigh in graph[i]:
            u = i
            v = neigh[0]
            w = neigh[1]
            if d[v] > (d[u] + w):
                return False

    return True

graph = read_graph_as_neigh_list_w()
k1 = list(graph.keys())[0]


print(Bellman_Ford_yes_or_not_negative_cycle(graph, k1))
'''3
> 4 2 -3
< 32 4 6
> 24 2 4'''
'''3
< 1 2 1
< 2 3 1
< 3 1 -3

пример с семенара'''
# Ввод след образом: 1- ая строка - колличество условий
# Все послед строки: 1-ый знак < или > (подразумевается не строгий), 2-ое число l,потом r и k

