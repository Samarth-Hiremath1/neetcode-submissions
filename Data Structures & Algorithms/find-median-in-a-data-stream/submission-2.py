class MedianFinder:

    def __init__(self):
        # 2 heaps
        # small: maxHeap
        # large: minHeap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # step 1: add to one of the heaps
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        # step 2: re-order size of heaps
        # if large > small by 2, popMin from large, push into small
        # if snall > large by 2, popMax from small, push into large

        if len(self.small) > len(self.large) +1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        

    def findMedian(self) -> float:
        # check if a heap is larger, take the min/max of it
        # else, take min/max of both and divide by 2

        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]

        return ((-1*self.small[0]) + (self.large[0])) / 2.0
        
        