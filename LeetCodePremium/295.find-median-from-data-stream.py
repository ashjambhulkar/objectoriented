#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        #here if the two arrays are of same size then we will first insert into the small array and then pop and push into the large one. We are mainly focusing on the large array instead of focusing on the small one
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        #here we are performing the reverse of the above logic
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))


            
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0])/2.0
        else:
            return float(self.large[0])
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

