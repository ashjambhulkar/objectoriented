#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key= lambda x:x[0])
        # result = []
        # for interval in intervals:
        #     if not result or result[-1][1] < interval[0]:
        #         result.append(interval)
        #     else:
        #         result[-1][1] = max(result[-1][1], interval[1])
        # return result


        intervals.sort(key= lambda x:x[0])
        result = [intervals[0]]
        for x in range(1, len(intervals)):
            if result[-1][1] >= intervals[x][0]:
                result[-1][1] = max(result[-1][1], intervals[x][1])
            else:
                result.append(intervals[x])

        return result
 
      
# @lc code=end

