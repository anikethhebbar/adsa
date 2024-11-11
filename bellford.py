# Bellman-Ford algorithm finds shortest paths from source to all vertices
# Also detects negative weight cycles
# Time complexity: O(VE) where V is number of vertices and E is number of edges
# Space complexity: O(V) for the distance array
def bellman_ford(graph, source, V):
    # Set initial distances to infinity except source vertex which is set to 0
    # This represents that we currently can't reach any vertices except source
    dist = [float("inf")] * V
    dist[source] = 0

    # Relax edges V-1 times because shortest path can have at most V-1 edges
    # Each iteration finds shortest paths using up to i edges
    for _ in range(V - 1):
        for u, v, w in graph:
            # If we can improve the distance to v by going through u
            # Then update distance to v
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles by trying to relax edges one more time
    # If any distance can still be reduced, there must be a negative cycle
    for u, v, w in graph:
        if dist[u] + w < dist[v]:
            return None  # Negative cycle exists
    return dist

# Get number of vertices and edges from user
V = int(input("Vertices: "))
E = int(input("Edges: "))

# Build graph as edge list where each edge is [u,v,w]
# u is source vertex, v is destination vertex, w is edge weight
graph = []
print("Enter edges (u v w):")
for _ in range(E):
    # Get space-separated u, v, w values and convert to integers
    u, v, w = map(int, input().split())
    graph.append([u, v, w])

# Get source vertex and run Bellman-Ford algorithm
source = int(input("Source: "))
distances = bellman_ford(graph, source, V)

# Print shortest path distances if no negative cycle
# Otherwise print error message
if distances:
    print(f"\nDistances from vertex {source}:")
    for i, d in enumerate(distances):
        print(f"{i}: {d}")
else:
    print("Negative cycle detected")

# Sample input/output:
# Vertices: 5 
# Edges: 8
# Enter edges (u v w):
# 0 1 -1  # Edge from vertex 0 to 1 with weight -1
# 0 2 4   # Edge from vertex 0 to 2 with weight 4
# 1 2 3   # Edge from vertex 1 to 2 with weight 3  
# 1 3 2   # Edge from vertex 1 to 3 with weight 2