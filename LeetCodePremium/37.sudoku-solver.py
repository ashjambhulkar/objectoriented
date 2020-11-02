#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
import collections

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)

        rows, cols, boxes = collections.defaultdict(
            set), collections.defaultdict(set), collections.defaultdict(set)
        
        for r in range(n):
            for c in range(n):
                if board[r][c]!= ".":
                    val = int(board[r][c])
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3)*3+c//3].add(val)


        def backtrack(r, c):
            if r == n-1 and c == n:
                return True
            
            if c == n:
                c = 0
                r += 1

            if board[r][c] != ".":
                return backtrack(r, c+1)
            
            box_id = (r//3)*3+c//3
            for v in range(1, n+1):
                if v not in rows[r] and v not in cols[c] and v not in boxes[box_id]:
                    board[r][c] = str(v)
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[box_id].add(v)

                    if backtrack(r, c+1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(v)
                    cols[c].remove(v)
                    boxes[box_id].remove(v)
            return False
        backtrack(0,0)

     
# @lc code=end

