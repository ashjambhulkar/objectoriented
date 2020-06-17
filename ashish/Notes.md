# 1. Data Structures

## 1.1. Disjoint Set and Union (DSU):
The most famous algorithm is `Kruskal Algorithm` which detect cycle in graph

Disjoint set perform two operations:
1. Find 
2. Union
  
**Find:** Detects elements that it belongs to which set

**Union:** It adds an edge in between the element find by the `Find` method if they belongs to two different set.
So in case of union if we find out that both the element onto which we are performing union are from same set then there is `cycle` in the graph.