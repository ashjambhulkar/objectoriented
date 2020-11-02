#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones):
        hashset = {}
        for i in range(len(stones)):
            hashset[stones[i]] = set()
        hashset[0].add(0)

        for i in range(len(stones)):
            for j in hashset[stones[i]]:
                for k in [j-1,j+1,j]:
                    if k > 0 and k+stones[i] in hashset:
                        hashset[k+stones[i]].add(k)
        return len(hashset[stones[-1]]) > 0


arr = [0, 1, 3, 4, 5, 7, 9, 10, 12]
Solution().canCross(arr)

# @lc code=end

