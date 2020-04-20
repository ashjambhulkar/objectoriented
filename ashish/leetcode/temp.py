import collections


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        def dfs(word):
            tmp.append(word)
            if word == endWord:
                res.append(list(tmp))
                tmp.pop()
                return
            if word in graph:
                for nei in graph[word]:
                    if dist[nei] == dist[word]+1:
                        dfs(nei)
            tmp.pop()

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        q = collections.deque([(beginWord, 0)])
        dist = {}
        graph = collections.defaultdict(set)
        seen = set([beginWord])
        while q:
            u, d = q.popleft()
            dist[u] = d
            for i in range(len(u)):
                for alph in alphabets:
                    if alph != u[i]:
                        new = u[:i]+alph+u[i+1:]
                        if new in wordSet:
                            graph[u].add(new)
                            graph[new].add(u)
                            if new not in seen:
                                q.append((new, d+1))
                                seen.add(new)
        if endWord not in dist:
            return []
        res = []
        tmp = []
        dfs(beginWord)
        return res
