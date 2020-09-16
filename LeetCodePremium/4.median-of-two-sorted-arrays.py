#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        lo = 0
        hi = len(A)
        while lo <= hi:
            # Find Partition in A using a regular binary search method.
            midA = (hi+lo)//2
            A_left = A[midA-1] if midA != 0 else float('-inf')
            A_right = A[midA] if len(A) != midA else float('inf')

            # Partition index in B derived from A, and moves in opposite direction of Partition A
            # - Median Index is usually midway somewhere, so here should be ~ Total // 2. And we know that:
            # - midA + midB = Total // 2
            # - midB = Total // 2 - midA
            midB = total//2 - midA
            B_left = B[midB-1] if midB != 0 else float('-inf')
            B_right = B[midB] if len(B) != midB else float('inf')

            # If both lefts are less than both rights, ideal partition detected.
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 0:
                    return max(A_left, B_left)/2.0 + min(A_right, B_right)/2.0
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:                          # A is too big   --> Reduce A partition size
                hi = midA-1
            # A is too small --> Increase A partition size (thereby reducing B)
            elif A_left < B_right:
                lo = midA+1
        return None

# @lc code=end

