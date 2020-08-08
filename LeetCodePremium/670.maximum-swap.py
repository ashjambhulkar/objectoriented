#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        test = [int(d)for d in str(num)]
        temp = {test[i]: i for i in range(len(test))}

        for i in range(len(test)-1
        ):
            maximum = max(test[i+1:])
            if maximum != test[i] and maximum > test[i]:
                test[temp[maximum]], test[i] = test[i],test[temp[maximum]]
                break
        return int(''.join(map(str, test)))
       

Solution().maximumSwap(98368)
# @lc code=end

