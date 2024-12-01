class Graph:
    def __init__(self):
        self.vertices = []
        self.adj_matrix = []

    def get_graph(self):
        n = int(input("Enter the number of vertices: "))
        self.adj_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            self.vertices.append(input(f"Enter label for vertex {i+1}: "))

        print("Enter edges: ")
        
        while True:
            v1 = input("Enter V1: ")
            v2 = input("Enter V2: ")

            if v1 == "" or v2 == "":
                break

            d = float(input("Enter the distance between V1 and V2: "))

            v1 = self.vertices.index(v1)
            v2 = self.vertices.index(v2)

            self.adj_matrix[v1][v2] = d

    def dijkstras(self, start):
        paths = {v: {'previous': None, 'distance': 0 if start == v else float('inf')} for v in self.vertices}
        unvisited = [v for v in self.vertices]

        while unvisited:
            curr = min(unvisited, key=lambda x: paths[x]['distance'])

            idx = self.vertices.index(curr)
            dist_to_current = paths[curr]['distance']

            for neighbour in range(len(self.vertices)):
                if self.adj_matrix[idx][neighbour] != float('inf') and self.vertices[neighbour] in unvisited:
                    dist_to_next = dist_to_current + self.adj_matrix[idx][neighbour]

                    if dist_to_next < paths[self.vertices[neighbour]]['distance']:
                        paths[self.vertices[neighbour]]['previous'] = curr
                        paths[self.vertices[neighbour]]['distance'] = dist_to_next
            
            unvisited.remove(curr)

        for vertex in paths:
            if vertex == start:
                continue
            path = []
            current = vertex
            while current is not None:
                path.append(current)
                current = paths[current]['previous']
            path.reverse()
            print(f"Path to {vertex}: {'->'.join(path)}")

g = Graph()
g.get_graph()
g.dijkstras(input("Enter start: "))
