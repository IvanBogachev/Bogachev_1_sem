def read_graph_as_edges():
    n = int(input())
    graph_prev = [list(map(str, input().split())) for i in range(n)]
    graph = []
    for i in range(n):
        if graph_prev[i][0] == "<":
            graph.append([int(graph_prev[i][1]), int(graph_prev[i][2]), int(graph_prev[i][3])])
        else:
            graph.append([int(graph_prev[i][2]), int(graph_prev[i][1]), (-1)*int(graph_prev[i][3])])
    return graph

def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges()
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



def Bellman_Ford_yes_or_not_negative_sycle(graph, s):
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
print(Bellman_Ford_yes_or_not_negative_sycle(graph, k1))

# Следующий принцип ввода:
# 1-строка - колличество условий
# далее в каждой строке: 1)-ый символ < / > (знаки не строгие), 2-ое число - l, 3-е число - r, 4-ое число - k

"""3
> 9 3 5
< 4 2 1
> 24 5 2

True
"""


"""3
< 5 64 1
< 64 41 1
< 41 5 -3
> 23 5 -2

False (Подобие того, что ты разбирал в пятницув 12.04.24)
"""