class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
      result = [0]
      for i in range(1, len(nums)):
        test = nums[i]-nums[i-1]-1+result[-1]
        result.append(test)
      left, value = 0, 0
      print(result)
      for i in range(1, len(result)):
        if result[i-1] <= k <= result[i]:
          return nums[i-1] + (k-result[i-1])
      return nums[-1] + k - result[-1]
