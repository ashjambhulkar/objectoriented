def helper(arr, k):
  hashmap = collections.defaultdict(int)
  count = 0
  start = 0
  for end in range(len(arr)):
    end_num = arr[end]
    hashmap[end_num] += 1
    count = max(count, hashmap[end_num])
    if end-start+1 - count > 1:
      