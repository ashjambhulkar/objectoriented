#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlength = 0
        hashmap = {0: 0}

        for line in input.split("\n"):
            dir_name = line.lstrip("\t")
            depth = len(line) - len(dir_name)
            if "." in dir_name:
                maxlength = max(maxlength, hashmap[depth]+len(dir_name))
            else:
                hashmap[depth+1] = hashmap[depth] + len(dir_name) + 1
        return maxlength
        
# @lc code=end

