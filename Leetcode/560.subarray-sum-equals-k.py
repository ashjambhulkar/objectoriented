#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashtable to track the sum of the integers from start
        sample  = collections.defaultdict(int)
        # initialize the first integer if the number is equalt to the target
        sample[0] = 1
        count = 0
        total = 0
        for x in range(len(nums)):
            # here we are taking sum of each number from the begining
            total += nums[x]
            # subtracting the nubmer from the target and checking how many times the resulting number appeared in the sample
            if total - k in sample:
                # counting all those number of occurances in the count
                count += sample[total-k]
            # incrementing the sample hash with the new total value
            sample[total] += 1  
        return count
        
# @lc code=end

