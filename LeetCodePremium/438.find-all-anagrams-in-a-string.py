#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        start = 0
        hashmap = collections.defaultdict(int)
        match = 0
        for end in range(len(s)):
            end_char = s[end]
            hashmap[end_char] += 1
            if end_char in p:
                match += 1
            while len(hashmap) > len(p):
                start_char = s[start]
                hashmap[start_char] -= 1
                if hashmap[start_char] == 0:
                    del hashmap[start_char]
                if start_char in p:
                    match -= 1
                start += 1
            if match == len(p):
                result.append(start)
        return result
        
# @lc code=end

