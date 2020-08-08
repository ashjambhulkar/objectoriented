#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#

# @lc code=start
class Solution:
    def numTeams(self, rating):
        count = 0
        for i, v in enumerate(rating[1:-1]):
            lmax, lmin, rmax, rmin = 0, 0, 0, 0
            for l in rating[:i+1]:
                if l < v:
                    lmin += 1
                elif l > v:
                    lmax += 1
            for r in rating[i+2:]:
                if r > v:
                    rmax += 1
                elif r < v:
                    rmin += 1
            count += lmin * rmax + lmax*rmin
        return count

        
# @lc code=end

