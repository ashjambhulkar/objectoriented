#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir = 0
        x = y = 0
        for i in instructions:
            if i == "L":
                dir = (dir+3)%4
            elif i == "R":
                dir = (dir+1)%4
            else:
                x += directions[dir][0]
                y += directions[dir][1]
        return (x == 0 and y == 0) or dir != 0

# @lc code=end

