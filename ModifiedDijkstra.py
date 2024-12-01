import heapq
import pprint
def dijkstra(graph,start,end):
    # Priority queue to store (distance, vertex) tuples
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_vertex={vertex:None for vertex in graph}
    visited = set()
    
    while queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(queue)
        
        if current_vertex in visited:
            continue

        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertex[neighbor]=current_vertex
                heapq.heappush(queue, (distance, neighbor))

        path=[]
        current_vertex=end
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex=previous_vertex[current_vertex]

        path=path[::-1]

    return distances[end],path



def get_graph():
    graph={}
    vertices=int(input("Enter the number of vertices:"))
    weights=[]

    for i in range(vertices):
        v=input("Enter the Vertex:")
        graph[v]={}
        edges=int(input(f"Enter number of edges from {v}:"))

        for j in range(edges):
            neighbor,weight=input(f"Enter neighbor and weight(seperated by space)").split()
            weight=int(weight)
            weights.append(weight)
            graph[v][neighbor]=int(weight)
     
    min_weight=abs(min(weights))

    for i in graph:
        for j in graph[i]:
            graph[i][j]+=min_weight    
    return graph

graph=get_graph()
print("Input Graph:")
pprint.pprint(graph)

start=input("Enter start node:")
end=input("Enter end node:")
distance,path= dijkstra(graph, start, end)
print(f"Shortest Path from node {start} to {end} is {path} with total weight {distance}")

