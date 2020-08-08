#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      # O(N^2) | O(M)
        # result = []
        # for x in nums1:
        #   i = nums2.index(x)
        #   temp = -1
        #   for y in nums2[i+1:]:
        #     if y > x:
        #       temp = y
        #       break
        #   result.append(temp)
        # return result

      # Time complexity: O(m+n). The entire numsnums array(of size n) is scanned only once. The stack's n elements are popped only once. The findNumsfindNums array is also scanned only once.


      # Space complexity: O(m+n). stackstack and mapmap of size n is used. resres array of size m is used, where n refers to the length of the numsnums array and m refers to the length of the findNumsfindNums array. 

        stack = []
        hashmap = collections.defaultdict(int)
        start = 0
        result = []
        while start < len(nums2):
          if stack and nums2[start] > stack[-1]:
            hashmap[stack.pop()] = nums2[start]
          else:
            stack.append(nums2[start])
            start += 1
        
        while stack:
          hashmap[stack.pop()] = -1
        
        for x in nums1:
          result.append(hashmap[x])
        
        return result


        
# @lc code=end


