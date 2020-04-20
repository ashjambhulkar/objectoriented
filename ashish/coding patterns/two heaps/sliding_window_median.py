import heapq


class SlidingWindowMedian:
  def __init__(self):
    self.maxHeap = []
    self.minHeap = []
    self.result = []

  def recorrect(self):
    if len(self.maxHeap) > len(self.minHeap)+1:
      heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

  def remove(self, heap, element):
    ind = heap.index(element)
    heap[ind] = heap[-1]
    del heap[-1]

    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
      heapq._siftup(heap, ind)
      heapq._siftdown(heap, 0, ind)

  def find_median(self, arr, k):
    for i in range(len(arr)):
      if not self.maxHeap or -self.maxHeap[0] >= arr[i]:
        heapq.heappush(self.maxHeap, -arr[i])
      else:
        heapq.heappush(self.minHeap, arr[i])

      self.recorrect()
      if i - k + 1 >= 0:
        if len(self.maxHeap) == len(self.minHeap):
          self.result.append((self.minHeap[0]-self.maxHeap[0])/2.0)
        else:
          self.result.append(-self.maxHeap[0]/1.0)
        if arr[i - k + 1] <= -self.maxHeap[0]:
          self.remove(self.maxHeap, -arr[i - k + 1])
        else:
          self.remove(self.minHeap, arr[i - k + 1])
        self.recorrect()

    return self.result


arr = [1, 2, -1, 3, 5]
k = 2
print(SlidingWindowMedian().find_median(arr, k))
