## Eulerians Path
An Eulerian path (or Eulerian Trail) is a path of edges that visits all the edges in a graph exactly once.


Choose any starting vertex v, and follow a trail of edges from that vertex until returning to v. It is not possible to get stuck at any vertex other than v, because indegree and outdegree of every vertex must be same, when the trail enters another vertex w there must be an unused edge leaving w.
The tour formed in this way is a closed tour, but may not cover all the vertices and edges of the initial graph.
As long as there exists a vertex u that belongs to the current tour, but that has adjacent edges not part of the tour, start another trail from u, following unused edges until returning to u, and join the tour formed in this way to the previous tour

Thus the idea is to keep following unused edges and removing them until we get stuck. Once we get stuck, we backtrack to the nearest vertex in our current path that has unused edges, and we repeat the process until all the edges have been used. We can use another container to maintain the final path.

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        if not tickets:
            return []
        graph = defaultdict(list)
        for o,d in tickets:
            graph[o].append(d)
        for o in graph:
            graph[o].sort(reverse=True)
        return self.helper(graph, 'JFK')
    
    def helper(self, graph, o):
        current_path = [o]
        trail = []
        while current_path:
            while current_path[-1] in graph:
                o = current_path[-1]
                d = graph[o]
                current_path.append(d.pop())
                if not d:
                    graph.pop(o)
            trail.append(current_path.pop())
        return trail[::-1]