#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        print(mapping)

# @lc code=end

digits = 23
def helper(digits):
    def combine(rst, remain_digits):
        #end condition
        if len(remain_digits) == 0: 
            return rst
        if len(rst) == 0:
            rst = ['']
        nxt_rst = []
        digit = remain_digits.pop(0)
        for r in rst:
            for c in mapping[digit]:
                nxt_rst.append(r+c)
        return combine(nxt_rst, remain_digits)  # nxt_rst = r+c

    return combine([],list(digits)) #first is current result

def actual(digits):
    def helper(digits, temp):
        if len(digits) == 0:
            return temp
        if len(temp) == 0:
            temp = ['']
        next_temp = []
        digit = digits.pop(0)
        for r in temp:
            for c in mapping[digits]:
                next_temp.append(r+c)
        return helper(digits, next_temp)