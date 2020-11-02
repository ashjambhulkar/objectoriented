#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.nums = [w[0]]
        for i in range(1, len(w)):
            self.nums.append(self.nums[-1]+w[i])
        

    def pickIndex(self) -> int:
        val = random.randrange(1, self.nums[-1]+1)
        lo, hi = 0, len(self.nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.nums[mid] < val:
                lo = mid+1
            else:
                hi = mid
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

