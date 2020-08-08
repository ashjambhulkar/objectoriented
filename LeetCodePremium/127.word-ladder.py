#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashmap = collections.defaultdict(list)

        for x in wordList:
            for i in range(len(beginWord)):
                hashmap[x[:i]+"*"+x[i+1:]].append(x)

        queue = collections.deque()
        queue.append((beginWord,1))
        visited = {beginWord: True}

        while queue:
            word, depth = queue.popleft()
            for i in range(len(beginWord)):
                temp = word[:i] + "*" + word[i+1:]
                for x in hashmap[temp]:
                    if x ==  endWord:
                        return depth+1
                    if x not in visited:
                        visited[x] = True
                        queue.append((x, depth+1))
                hashmap[temp] = []

        return 0


# @lc code=end

