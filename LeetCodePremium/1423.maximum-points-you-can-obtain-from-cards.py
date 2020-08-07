#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        k = len(cardPoints) - k
        temp = result = sum(cardPoints[:k])
        start = 0
        for end in range(k, len(cardPoints)):
          temp += cardPoints[end] - cardPoints[start]
          result = min(temp, result)
          start += 1
        return sum(cardPoints) - result
        
# @lc code=end

