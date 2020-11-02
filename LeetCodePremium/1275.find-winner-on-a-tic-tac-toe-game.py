#
# @lc app=leetcode id=1275 lang=python3
#
# [1275] Find Winner on a Tic Tac Toe Game
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows, cols, ldiagonal, rdiagonal, length = [0]*3, [0]*3, 0, 0, 3
        temp = -1
        for x, y in moves:
          rows[x] += temp
          cols[y] += temp
          if x == y:
            ldiagonal += temp
          if x+y == length-1:
            rdiagonal += temp
          if 3 in rows or 3 in cols or 3 in (ldiagonal, rdiagonal):
            return "B"
          if -3 in rows or -3 in cols or -3 in (ldiagonal, rdiagonal):
            return "A"
          temp = 0-temp
        if len(moves) < 9:
          return "Pending"
        return "Draw"
        
# @lc code=end

