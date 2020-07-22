#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        sample = collections.defaultdict(int)
        start = 0
        for end in range(len(s)):
            end_char = s[end]
            if end_char in sample:
                sample[end_char] -= 1
                if sample[end_char] == 0:
                    del sample[end_char]
            else:
                sample[end_char] += 1
            if len(sample) == 2:
                if s[start:end] == s[start:end][::-1]:
                    return True
            while len(sample) > 2:
                sample[s[start]] -= 1
                if sample[start] == 0:
                    del sample[start]
                start += 1
        return False

            

# @lc code=end

