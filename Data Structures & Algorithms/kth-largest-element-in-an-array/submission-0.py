import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)

        for i in range(k):
            res = -1 * heapq.heappop(h)
        return res