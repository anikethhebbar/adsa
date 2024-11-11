# Floyd-Warshall algorithm to compute the shortest paths between all pairs of vertices in a graph.
# The algorithm uses an adjacency matrix representation of the graph, which is provided by the user.

def floyd_warshall(graph, V):
    # Create a 2D list 'dist' to store the shortest distances between every pair of vertices.
    # Initially, set all distances to infinity, indicating no path between vertices.
    dist = [[float("inf")] * V for _ in range(V)]
    
    # Initialize the distance matrix with the given graph's adjacency matrix.
    for i in range(V):
        for j in range(V):
            if i == j:
                # The distance from any vertex to itself is zero.
                dist[i][j] = 0
            elif graph[i][j] != 0:
                # If there is a direct edge between vertex i and j, set the distance to the edge weight.
                dist[i][j] = graph[i][j]
    
    # Update the distance matrix to find the shortest paths using the Floyd-Warshall algorithm.
    # The algorithm considers each vertex as an intermediate point in potential paths.
    for k in range(V):
        # For each vertex k, update the shortest paths between all pairs of vertices i and j.
        for i in range(V):
            for j in range(V):
                # If a shorter path from i to j through k is found, update the distance.
                # This checks if the path from i to k and then k to j is shorter than the current known path from i to j.
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Return the matrix containing the shortest paths between all pairs of vertices.
    return dist

# Prompt the user to input the number of vertices in the graph.
V = int(input("Enter number of vertices: "))

# Initialize the adjacency matrix for the graph with zeros, indicating no direct edges initially.
graph = [[0] * V for _ in range(V)]

# Prompt the user to input the adjacency matrix, which represents the graph.
print("\nEnter the adjacency matrix (Enter 0 for no direct edge):")
for i in range(V):
    # Read each row of the adjacency matrix from user input.
    row = list(map(int, input().split()))
    for j in range(V):
        # Fill the adjacency matrix with the user-provided values.
        graph[i][j] = row[j]

# Compute the shortest paths between all pairs of vertices using the Floyd-Warshall algorithm.
distances = floyd_warshall(graph, V)

# Print the shortest distances between all pairs of vertices.
print("\nShortest distances between all pairs of vertices:")
for i in range(V):
    for j in range(V):
        if distances[i][j] == float("inf"):
            # Print 'INF' for pairs of vertices that are not reachable from each other.
            print("INF", end="\t")
        else:
            # Print the shortest distance between vertex i and j.
            print(distances[i][j], end="\t")
    # Move to the next line for the next row of distances.
    print()

# Sample input:
# Enter number of vertices: 4
# Enter the adjacency matrix:
# 0 5 0 10
# 0 0 3 0
# 0 0 0 1
# 0 0 0 0
