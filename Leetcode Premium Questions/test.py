import collections


# def helper(A, B):
#     ans = []
#     for b in B:
#         counter = 0
#         for a in A:
#             if b.count(min(b)) > a.count(min(a)):
#                 counter += 1
#         ans.append(counter)
#     return ans

# first = ["abcd","aabc","bd"]
# second = ["aaa","aa"]
# print(helper(first, second))



# def helper(arr, k):
#     start = 0
#     total = 0
#     maximum = float("-inf")
#     point = 0
#     for end in range(len(arr)):
#         total += arr[end]
#         if end-start+1 > k:
#             total -= arr[start]
#             start += 1
#         if total > maximum:
#             maximum = total
#             point = end
#     return arr[point-k+1:point+1]

# arr = [1,4,3,2,5,8,3,9,11]
# print(helper(arr, 4))



# def helper(string):
#     result = ""
#     temp = [2, 3, 0 , 5, 9]
#     for i in range(len(string)):
#         if string[i] == "?":
#             if i == 1 and int(result[0]) > 0:
#                 result += str(temp[1])
#             elif i == 1:
#                 result += "9"
#             else:
#                 result += str(temp[i])
#         else:
#             result += string[i]
#     return result


# print(helper("0?:5?"))



# def helper(string, result):
#     print(result)
#     for i in range(len(string)):
#         result.append(string[i])
#         helper(string[i+1:], result)
#         result.pop()

# a = ["J", "B", "M", "S"]
# helper(a, [])



# Google | OA 2019 | Most Booked Hotel Room
# import collections

# def helper(rooms):
#     result = collections.defaultdict(int)
#     for x in rooms:
#         if x[0] == "+":
#             result[x[1:]] += 1
#     temp = []
#     for key, value in result.items():
#         temp.append((value, key))
#     print(temp)
#     temp.sort(key=lambda x: (-x[0], x[1]))
#     print(temp)
#     print(temp[0][1])


# rooms = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E","+3E", "+3E", "-3E","-3E", "+2E", "+2E", "+2E"]
# print(helper(rooms))


# Google | OA 2019 | Watering Flowers 2.0

# def helper(arr, l, r):
#     start = 0
#     end = len(arr)-1
#     count = 2
#     left = l
#     right = r
#     while start < end:
#         if start == end and left+right < arr[start]:
#             count = count + 1
#         if arr[start] > left:
#             count += 1
#             left = l - arr[start]
#         else:
#             left = left - arr[start]
#         if arr[end] > right:
#             count += 1
#             right = r - arr[end]
#         else:
#             right -= arr[end]
#         start += 1
#         end -= 1
#     return count


# arr = [2,4,5,1,2,5,7,4]
# l = 5
# r = 7
# print(helper(arr, l, r))




# 0/1 KnapSack Problem

# Brute Force Recursion
# def knapsack(profits, weights, capacity):
#     # basic checks
#     n = len(profits)
#     if capacity <= 0 or n == 0 or len(weights) != n:
#         return 0

#     dp = [0 for x in range(capacity+1)]

#     # if we have only one weight, we will take it if it is not more than the capacity
#     for c in range(0, capacity+1):
#         if weights[0] <= c:
#             dp[c] = profits[0]

#     # process all sub-arrays for all the capacities
#     for i in range(1, n):
#         for c in range(capacity, -1, -1):
#             profit1, profit2 = 0, 0
#         # include the item, if it is not more than the capacity
#             if weights[i] <= c:
#                 profit1 = profits[i] + dp[c - weights[i]]
#             # exclude the item
#             profit2 = dp[c]
#             # take maximum
#             dp[c] = max(profit1, profit2)

#     return dp[capacity]



# profits = [1, 6, 10, 16]
# weights = [1,2,3,5]
# capacity = 7

# print(knapsack(profits, weights, capacity))

###1153. String Transforms Into Another String
#####not solved hard question

# import collections


# def helper(str1, str2):
#     if not str1:
#         return True
    
#     sample = collections.defaultdict(str)

#     for i in range(len(str1)):
#         sample[str1[i]] = str2[i]
    
#     print(sample)

#     for i in range(len(str1)):
#         if not (sample[str1[i]] == str2[i]):
#             return False
#     return True


# a = "abcdefghijklmnopqrstuvwxyz"
# b = "bcdefghijklmnopqrstuvwxyza"
# print(helper(a, b))


###482. License Key Formatting

# def helper(S,K):
#     sample = S.split("-")
#     sample = "".join(sample)
#     count = 0
#     result = ""
#     for i in range(len(sample)-1, -1, -1):
#         if count < K:
#             result = (sample[i]).upper() + result
#             count += 1
#         else:
#             result = (sample[i]).upper()+"-"+result
#             count = 1
#     return result


# S = "2-5g-3-J" 
# K = 2
# print(helper(S,K))


# https://leetcode.com/discuss/interview-question/350363/google-oa-max-distance

# from random import randint


# class TrieNode:
#     def __init__(self):
#         self.ch = collections.defaultdict(TrieNode)
#         self.end = False
#         self.h = 0  # longest tail from this node

#     def add(self, s):
#         node, n = self, len(s)
#         for i, b in enumerate(s):
#             node = node.ch[b]
#             node.h = max(node.h, n - i)
#         node.end = True

#     def dist(self, s):
#         node, n, cand = self, len(s), []
#         for i, b in enumerate(s):
#             # word in A reaches end
#             if node.end:
#                 cand.append(n - i)
#             # find the first mismatch
#             bb = '1' if b == '0' else '0'
#             if bb in node.ch:
#                 cand.append(n - i + node.ch[bb].h)
#             # go to next trie node
#             if b in node.ch:
#                 node = node.ch[b]
#                 continue
#             # nowhere to go, break
#             cand.append(n - i + node.h - 1)
#             break
#         else:
#             # word in B is substring of word in A
#             cand.append(node.h - 1)
#         return max(cand)


# def maxDistance(A, B):
#     if len(B) > len(A):
#         A, B = B, A
#     root = TrieNode()
#     for a in A:
#         root.add(a)
#     return max(root.dist(b) for b in B)


# def dist(a, b):
#     ans = len(a) + len(b)
#     for s, t in zip(a, b):
#         if s == t:
#             ans -= 2
#         else:
#             break
#     return ans


# trial = 10
# for _ in range(trial):
#     size_A, size_B = randint(1, 3), randint(1, 3)
#     A = [bin(randint(0, 1 << 6))[2:] for _ in range(size_A)]
#     A = [a.zfill(len(a) + randint(0, 3)) for a in A]
#     B = [bin(randint(0, 1 << 6))[2:] for _ in range(size_B)]
#     B = [b.zfill(len(b) + randint(0, 3)) for b in B]
#     d1 = max(dist(a, b) for a in A for b in B)
#     d2 = maxDistance(A, B)
#     if trial <= 10 or d1 != d2:
#         print(A, B)
#         print(f'brute: {d1}, maxDistance: {d2}')




# Min Days To Bloom:

# def helper(arr, n):
#   low = 0
#   high = len(arr)-1
#   while low < high:
#     mid = (low + high) // 2
#     if arr[mid] < n:
#       low = mid+1
#     else:
#       high = mid
#
#   return arr[high]
#
#
# arr = [1, 2, 4, 9, 3, 4, 1]
# print(helper(arr, 2))


#### validate stack sequenece

# def helper(pushed, popped):
#     result = []
#     i = 0
#     for x in pushed:
#         result.append(x)
#         while i < len(popped) and result[-1] == popped[i]:
#             result.pop()
#             i += 1
#     return len(result) == 0

# pushed = [1,0]
# popped = [1,0]

# print(helper(pushed, popped))


# class Solution:
#     def gridGame(self, grid, k, rules):
#         if not grid or grid == []:
#             return grid
#         if len(grid) == 0 or len(grid[0]) == 0:
#             return grid
#         rules = set(rules)

#         for i in range(k):
#             grid = self.updateGrid(grid, rules)

#         return grid

#     def updateGrid(self, grid, rules):
#         m, n = len(grid), len(grid[0])
#         new_grid = [[0 for _ in range(n)] for _ in range(m)]
#         directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
#                       (-1, -1), (-1, 1), (1, -1), (1, 1)]

#         for i in range(m):
#             for j in range(n):
#                 count = 0
#                 for di, dj in directions:
#                     if 0 <= i + di < m and 0 <= j + dj < n and grid[i+di][j+dj] == 1:
#                         count += 1
#                 if count in rules:
#                     new_grid[i][j] = 1

#         return new_grid


# s = Solution()
# grid = [[0, 1, 1, 0], [1, 1, 0, 0]]
# k = 2
# rules = [3, 5]

# print(s.gridGame(grid, k, rules))

# def helper(arr, limit):
#     lheap, rheap = [], []
#     result = 0
#     start = 0
#     for end, value in enumerate(arr):
#         heapq.heappush(lheap, (value, end))
#         heapq.heappush(rheap, (-value, end))
#         while -rheap[0][0] - lheap[0][0] > limit:
#             start = min(lheap[0][1], rheap[0][1])+1
#             while start > lheap[0][1]:
#                 heapq.heappop(lheap)
#             while start > rheap[0][1]:
#                 heapq.heappop(rheap)
#             result = max(result, end-start+1)
#     return result



#longestsubarray:
# def helper(A, limit):
#     maxq, minq = [], []
#     res = i = 0
#     for j, a in enumerate(A):
#         heapq.heappush(maxq, [-a, j])
#         heapq.heappush(minq, [a, j])
#         while -maxq[0][0] - minq[0][0] > limit:
#             i = min(maxq[0][1], minq[0][1]) + 1
#             while maxq[0][1] < i:
#                     heapq.heappop(maxq)
#             while minq[0][1] < i:
#                     heapq.heappop(minq)
#         res = max(res, j - i + 1)
#     return res


#659 split array into consecutive subsequences:

def helper(nums):
    # keep track of the frequency of each value in the nums
    counter, needs = collections.Counter(nums), collections.Counter()

    for num in nums:
        # in case we've previously used this value
        if not counter[num]:
            continue
        # in case if this value can be appended an existing sequence
        elif needs[num] > 0:
            needs[num] -= 1
            needs[num + 1] += 1
        # otherwise if this value can be used as the state of a new sequence
        elif counter[num + 1] > 0 and counter[num + 2] > 0:
            counter[num + 1] -= 1
            counter[num + 2] -= 1
            needs[num + 3] += 1
        # if either of above case can hold, then we cannot split this array
        # into consecutive subsequences
        else:
            return False

        # update counter for current value
        counter[num] -= 1

    return True

arr = [1,2,3,4,4,5,5,6,6]
print(helper(arr))