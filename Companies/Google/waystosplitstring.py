import collections


def helper(string):
    start = 0
    left = collections.Counter(string[0])
    right = collections.Counter(string[1:])
    count = 0
    for end in range(1, len(string)):
        if left.keys() == right.keys():
            count += 1
        start += 1
        left[string[start]] += 1
        if left[string[start]] == 0:
            del left[string[start]]
        right[string[end]] -= 1
        if right[string[end]] == 0:
            del right[string[end]]
    return count


string = "abcbca"
print(helper(string))
