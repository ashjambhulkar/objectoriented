#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.checkin = collections.defaultdict(tuple)
        self.averagetime = collections.defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkin:
            self.checkin[id] = (stationName, t)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin:
            y, x = self.checkin[id]
            self.averagetime[(y, stationName)].append(t-x)
            del self.checkin[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        x = self.averagetime[(startStation, endStation)]
        return sum(x)/len(x)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

