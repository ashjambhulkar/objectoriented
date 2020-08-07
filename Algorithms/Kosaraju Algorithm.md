## Kosaraju Algorithm

Kosaraju algorithm is to find the strongly connected components.
**1)** Create an empty stack ‘S’ and do DFS traversal of a graph. In DFS traversal, after calling recursive DFS for adjacent vertices of a vertex, push the vertex to stack. In the above graph, if we start DFS from vertex 0, we get vertices in stack as 1, 2, 4, 3, 0.  
**2)** Reverse directions of all arcs to obtain the transpose graph.  
**3)** One by one pop a vertex from S while S is not empty. Let the popped vertex be ‘v’. Take v as source and do DFS. The DFS starting from v prints strongly connected component of v. In the above example, we process vertices in order 0, 3, 4, 2, 1 (One by one popped from stack).

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/SCC.png)


![Strongly connected components](https://cdn.programiz.com/sites/tutorial2program/files/scc-strongly-connected-components.png)




```
import collections

class Graph:
    def __init__(self, vertex):
        self.v = vertex
        self.graph = collections.defaultdict(list)

    # add edge into the Graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited):
        visited[d] = True
        print(d)
        for i in self.graph[d]:
            if not visited[i]:
                self.dfs(i, visited)
    

    def fill_order(self, d, visited, stack):
        visited[d] = True
        for i in self.graph[d]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack.append(d)

    # Transponse the matrix

    def transpose(self):
        g = Graph(self.v)
        
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    
    # print strongly connected components
    def print_sccs(self):
        stack = []
        visited = [False] * self.v

        for i in range(self.v):
            if not visited[i]:
                self.fill_order(i, visited, stack)
        
        gr = self.transpose()

        visited = [False] * self.v

        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.dfs(i, visited)
                print("")
        

g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_sccs()


```