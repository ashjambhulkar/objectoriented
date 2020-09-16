#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # sample = [i for i in range(1, n+1)]
        # result = []
        # def helper(sample, temp):
        #     if len(temp) == k:
        #         result.append(temp[:])
        #     elif len(temp) <= k:  
        #         for i in range(len(sample)):
        #             temp.append(sample[i])
        #             helper(sample[i+1:],temp)
        #             temp.pop()
        # helper(sample, [])
        # return result
        sample = [i for i in range(1, n+1)]
        result = []
        def helper(sample, temp):
            if len(temp) == k:
                result.append(temp[:])
            for i in range(len(sample)):
                temp.append(sample[i])
                helper(sample[i+1:], temp)
                temp.remove(sample[i])
        helper(sample, [])
        return result


# @lc code=end

