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

def Dijkstra(graph, v):
    d = {}
    queue = []
    visited = []
    for key in graph.keys():
        d[key] = 1000

    d[v] = 0
    queue.append([0, v])

    while queue:
        queue.sort()
        print("queue1 =", queue)

        c = queue.pop(0)
        print("queue2 =", queue)
        visited.append(c[1])
        print('visited =', visited)
        for neigh in graph[c[1]]:
            if neigh[0] not in visited:
                print("neigh =", neigh)
                print("c =", c)
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    print('d[c[1]] = ', d[c[1]], 'neigh[1] =', neigh[1], 'd[neigh[0]] =', d[neigh[0]])
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                    print("d2 = ", d)
                queue.append(neigh[::-1])
                print('neigh[::-1]', neigh[::-1])


                print("   "
                      "   ")
    return d
graph = read_graph_as_neigh_list_w()
#DFS_w(graph, 1)
# print(has_cycle(graph, 1))
# print(topologicalSort(graph))
print(Dijkstra(graph, 1))