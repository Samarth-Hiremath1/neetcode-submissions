import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        h = []
        for c in count.keys():
            heapq.heappush(h, (count[c], c))
            if len(h) > k:
                heapq.heappop(h)
            
        
        res = []
        for i in range(len(h)):
            res.append(heapq.heappop(h)[1])
        return res