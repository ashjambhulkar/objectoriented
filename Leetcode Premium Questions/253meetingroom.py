import heapq

def meetingroom(intervals):
  if not intervals:
    return 0

  intervals.sort(key=lambda x: x[0])

  result = []
  heapq.heappush(result, intervals[0][1])

  for x in intervals[1:]:
    if result[0] <= x[0]:
      heapq.heappop(result)
    heapq.heappush(result, x[1])
  
  return len(result)



# 2----------------11
#     6--------------------16
#                  11------16

# intervals = [[2, 11], [6, 16], [11, 16]]

# 0----------------------------------30
#      5------10
#                  15-----20

intervals = [[0, 30], [5, 10], [15, 20]]

print(meetingroom(intervals))

