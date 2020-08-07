#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        sample = [i for i in range(1, n+1)]
        result = []
        count = 0
        def helper(sample, temp):
            nonlocal count
            if len(sample) == 0:
                count += 1
                if count == k:
                    result.append(temp[:])
            elif count < k:       
                for i in range(len(sample)):
                    var = sample[i]
                    temp.append(var)
                    sample.remove(var)
                    helper(sample, temp)
                    temp.pop()
                    sample.insert(i, var)
        helper(sample, [])
        test = ""
        for x in result[0]:
            test += str(x)
        return test

        
# @lc code=end

