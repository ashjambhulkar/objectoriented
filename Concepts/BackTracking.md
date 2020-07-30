## A general approach to backtracking questions in Python (Subsets, Permutations, Combination Sum, Palindrome Partioning)

### Subsets

https://leetcode.com/problems/subsets/

## Stanford Lecture

https://www.bilibili.com/video/BV1Dt41117ET?p=8

  

### Calculate Binary Value of given number

```
def helper(nums, result):
    if nums == 0:
        print(result)
        return
    helper(nums-1, result+"0")
    helper(nums-1, result+"1")


helper(3, "")


Print Output:
000
001
010
011
100
101
110
111
```

### Calculate the the dice roll sum to target

```
def helper(nums, target, result):
    if nums == 0:
        if target == 0:
            print(result)
        return
    for i in range(1,  7):
        result.append(i)
        helper(nums-1, target-i, result)
        result.pop()

helper(3, 7, [])

Print Output:
[1, 1, 5]
[1, 2, 4]
[1, 3, 3]
[1, 4, 2]
[1, 5, 1]
[2, 1, 4]
[2, 2, 3]
[2, 3, 2]
[2, 4, 1]
[3, 1, 3]
[3, 2, 2]
[3, 3, 1]
[4, 1, 2]
[4, 2, 1]
[5, 1, 1]
```

### Calculate all the permutations of the given string

```
def helper(nums, result):
  if not nums:
    print(result)
    return
  for i in range(len(nums)):
    var = nums[i]
    result.append(var)
    nums.remove(var)
    helper(nums, result)
    result.pop()
    nums.insert(i, var)


helper([1,2,3], [])

Print Output:
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
```