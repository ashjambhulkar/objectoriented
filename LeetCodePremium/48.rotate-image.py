#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Transpose matrix 
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
         
        #reverse each row
        for i in range(len(matrix[0])):
            matrix[i].reverse()

# @lc code=end

