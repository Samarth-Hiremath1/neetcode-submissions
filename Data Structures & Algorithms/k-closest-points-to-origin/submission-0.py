# points = [[0,2],[2,2]], k = 1


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        heapq.heapify(minHeap)

        for x, y in points:
            dist = (x **2 ) + (y**2)
            heapq.heappush(minHeap, (-dist, x, y))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        

        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res
