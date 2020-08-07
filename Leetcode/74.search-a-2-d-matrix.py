#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start

# The condition in the description "The first integer of each row is greater than the last integer of the previous row." makes this 2d array as 1d sorted array. Merge sort is the best alogrithm to find an element in sorted array. 

class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		if not matrix:
			return False
		row, col = len(matrix), len(matrix[0])
		left, right = 0, row*col-1
		while left <= right:
			pivot = (left + right) // 2
			# Calculation of pivot element is the most important point here, rest is just following the merge sort algorithm.
			pivot_element = matrix[pivot// col][pivot % col]
			
			if pivot_element == target:
				return True
			else:
				if pivot_element < target:
					left = pivot + 1
				else:
					right = pivot - 1
		return False
        
# @lc code=end

