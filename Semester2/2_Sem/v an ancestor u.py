def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_neigh_list():
    edge_list = read_graph_as_edges()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    #print(V_num)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        if edge[0] not in graph_dict.keys():
            graph_dict[edge[0]] = frozenset([edge[1]])
        else:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([edge[1]])
    return graph_dict


def DFS(graph, v, visited=[]):
    print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS(graph, neigh, visited)


def topologicalSortUtil(graph, v, visited, stack):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
                topologicalSortUtil(graph, i, visited, stack)


    stack.insert(0, v)


def topologicalSort(graph):

    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if visited[i] == False:
            topologicalSortUtil(graph, i, visited, stack)
    return stack



graph = read_graph_as_neigh_list()
topological_sort = topologicalSort(graph)
top = topological_sort[0] #<-- корень
dict = {}
def children(graph,top):
    s = set()
    for neigh in graph[top]:
        s = s | children(graph, neigh)
    dict[top] = s
    s.add(top)

    return s
children(graph,top)
def way(dict, v, u): #есть ли путь из v в u?
    if u in dict[v]:
        return "Yes"
    else:
        return "No"

print(way(dict,2,5))


'''10
0 1
1 2
1 3
2 4
2 7
3 5
3 4
4 6
4 8
8 6'''




















