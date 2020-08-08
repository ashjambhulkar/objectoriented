#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = collections.Counter(words)

        result = []
        temp = []

        for key, value in hashmap.items():
            heapq.heappush(result, (-value, key))
        
        for _ in range(k):
            value, key = heapq.heappop(result)
            temp.append(key)
        
        return temp
# @lc code=end

