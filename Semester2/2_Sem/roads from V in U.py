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
    print(V_num)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        if edge[0] not in graph_dict.keys():
            graph_dict[edge[0]] = frozenset([edge[1]])
        else:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([edge[1]])
    return graph_dict


def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = 1

    return res_matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)


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


def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = 1

    return res_matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)

def DFS(graph, v, visited=[]):
    print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS(graph, neigh, visited)


def has_cycle(graph, v, visited=[]):
    result = False
    visited.append(v)

    for neigh in graph[v]:

        if neigh in visited:
            result = True
            return result

        if result == False:
            result = has_cycle(graph, neigh, visited)

    return result


def DFS_stack(graph, v, visited=[]):
    stack = []
    visited.append(v)
    stack.append(v)
    while stack:
        v = stack.pop()
        print(v)
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                stack.append(neigh)

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



def processing(graph, v, u):   #колличество путей из v в u
    topological_sort = topologicalSort(graph)
    if topological_sort.index(v) > topological_sort.index(u):
        return "Путей нет"
    else:
        working_vertices = []
        for i in range(topological_sort.index(v),topological_sort.index(u) + 1):
            working_vertices.append(topological_sort[i])
        return working_vertices

def find_way(graph,working_vertices,u,v):
    s = 0
    if u not in working_vertices:
        return 0
    elif u == v:
        return 1
    else:
        for neigh in graph[u]:
            s += find_way(graph,working_vertices,neigh,v)

    return s



graph = read_graph_as_neigh_list()

print(find_way(graph,processing(graph,7,3),7,3))




