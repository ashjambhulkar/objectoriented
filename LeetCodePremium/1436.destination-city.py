#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
      	hashset = set()
      	for x, y in paths:
        	hashset.add(y)

      	for x, y in paths:
        	if x in hashset:
          		hashset.remove(x)
      	return hashset.pop()
        
# @lc code=end

