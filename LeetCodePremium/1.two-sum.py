#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = collections.defaultdict(list)
        
        # for i, x in enumerate(nums):
        #     hashmap[x].append(i)
        
        # for i, x in enumerate(nums):
        #     if target-x in hashmap:
        #         for j in hashmap[target-x]:
        #             if j != i:
        #                 return [i,j]
                    
        # return -1












        sample = collections.defaultdict(int)
        
        for i, v in enumerate(nums):
            sample[v] = i

        for i, x in enumerate(nums):
            temp = target-x
            if temp in sample and sample[temp] != i:
                return [i, sample[temp]
                ]
        return -1


        
# @lc code=end

