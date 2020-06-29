#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashmap = collections.defaultdict(int)
        banned = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c," ")
        paragraph = paragraph.lower().split()

        for word in paragraph:
            if word not in banned:
                hashmap[word] += 1
        
        return max(hashmap, key=hashmap.get)

# @lc code=end

