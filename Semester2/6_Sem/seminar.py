def read_graph_as_edges():
    n = int(input())
    graph = [list(map(str, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return  graph
def read_graph_as_neigh_list():
    edge_list = read_graph_as_edges()
    graph_dict = {} #dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        if edge[0] not in graph_dict.keys():
            graph_dict[edge[0]] = frozenset([edge[1]])
        else:
            graph_dict[edge[0]]= graph_dict[edge[0]] | frozenset([edge[1]])
    return graph_dict

def have_cycle(adj_list, u, colors):
    ans = False
    colors[u] = 'grey'
    for v in adj_list[u]:
        if colors[v] == "white":
            have_cycle(adj_list, v, colors)
        if colors[v] == "grey":
            ans = True
            return ans
    colors[u] = 'black'
    return ans


graph = read_graph_as_edges()
colors = []
for i in range(len(graph) + 1):
    colors.append("white")
print(graph)

'''3
1 2
2 3
1 3'''