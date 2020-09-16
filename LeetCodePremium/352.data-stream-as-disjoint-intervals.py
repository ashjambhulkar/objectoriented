#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start
class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.seen = set()
        

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])

    def getIntervals(self) -> List[List[int]]:
        stack = []
        while self.intervals:
            cur = heapq.heappop(self.intervals)
            if stack and cur[0] <= stack[-1][1]+1:
                stack[-1][1] = max(stack[-1][1], cur[1])
            else:
                stack.append(cur)
        self.intervals = stack
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

