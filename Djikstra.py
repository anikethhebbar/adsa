#djikstra algorithm to find the shortest path in a graph using user inputs

def djikstra(graph, start, end):
    # Initialize distances
    dist = [float("inf")] * len(graph)
    dist[start] = 0

    # Initialize visited nodes
    visited = [False] * len(graph)

    # Find shortest path
    for _ in range(len(graph)):
        min_dist = float("inf")
        min_index = -1
        for i in range(len(graph)):
            if dist[i] < min_dist and not visited[i]:
                min_dist = dist[i]
                min_index = i
        if min_index == -1:
            break
        visited[min_index] = True
        for i in range(len(graph)):
            if not visited[i] and graph[min_index][i] != 0 and dist[min_index] + graph[min_index][i] < dist[i]:
                dist[i] = dist[min_index] + graph[min_index][i]

    return dist[end]

#read the graph from the user
graph = []
for i in range(len(graph)):
    graph.append(list(map(int, input().split())))

print(djikstra(graph, 0, 4))

#sample input output 
# 0 1 4 0 0
# 1 0 4 2 2
# 4 4 0 3 1
# 0 2 3 0 0
# 0 2 1 0 0
#output 3