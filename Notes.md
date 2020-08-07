# 1. Data Structures

## 1.1. Disjoint Set and Union (DSU):
The most famous algorithm is `Kruskal Algorithm` which detect cycle in graph

Disjoint set perform two operations:
1. Find 
2. Union
  
**Find:** Detects elements that it belongs to which set

**Union:** It adds an edge in between the element find by the `Find` method if they belongs to two different set.
So in case of union if we find out that both the element onto which we are performing union are from same set then there is `cycle` in the graph.



code for letter combination:

def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


        def helper(result, digits):
            if not digits:
                return result
            if not result:
                result = ['']
            first = digits.pop(0)
            intermediate = []
            for r in result:
                for c in mapping[first]:
                    intermediate.append(r+c)
            return helper(intermediate, digits)
        return helper([], list(digits))


if None in (l1, l2):
    return l1 or l2