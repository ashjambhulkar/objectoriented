class Solution:
    def findNonRep(self, nums):
        result = [0]
        for i in (1, len(nums)-1,1):
            test = nums[i]-nums[i-1]-1+result[-1]
            print(result)
            result.append(test)
        print(result)


test = [4, 7, 9, 10]

print(Solution().findNonRep(test))
