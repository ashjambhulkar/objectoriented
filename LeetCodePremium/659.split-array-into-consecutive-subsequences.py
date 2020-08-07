#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        a = collections.Counter(nums)
        b = collections.Counter()
        for x in nums:
            if a[x] == 0:
                continue

            elif b[x] > 0:
                b[x] -= 1
                b[x+1] += 1

            elif a[x+1] > 0  and a[x+2] > 0:
                a[x+1] -= 1
                a[x+2] -= 1
                b[x+3] += 1
            else:
                return False
            a[x] -= 1
        return True

        
        
# @lc code=end

