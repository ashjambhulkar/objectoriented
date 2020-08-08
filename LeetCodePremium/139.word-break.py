#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashset = set(wordDict)
        visited = [0] * len(s)
        queue = collections.deque()
        queue.append(0)
        while queue:
            start = queue.pop()
            if visited[start] == 0:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in hashset:
                        queue.append(end)
                        if end == len(s):
                            return True
                visited[start] = 1
        return False
        
# @lc code=end

