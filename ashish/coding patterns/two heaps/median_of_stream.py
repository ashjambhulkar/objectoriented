import heapq

class MedianOfStream:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def insert(self, num):
        if not self.maxHeap and -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
    
        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        else:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
    

    def get_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2.0
        else:
            return -self.maxHeap[0]