class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
      slots1 = sorted(filter(lambda x: x[1]-x[0] >= duration, slots1))
      slots2 = sorted(filter(lambda x: x[1]-x[0] >= duration, slots2))

      i = j = 0

      while i < len(slots1) and j < len(slots2):
        start1, end1 = slots1[i]
        start2, end2 = slots2[j]

        if start1 >= start2 and start1+duration <= end2:
          return [start1, start1+duration]
        if start2 >= start1 and start2+duration <= end1:
          return [start2, start2+duration]
        if end1 < end2:
          i += 1
        else:
          j += 1
      return []


