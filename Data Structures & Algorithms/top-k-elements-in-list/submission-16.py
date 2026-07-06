class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # val: counts 
        freq = [[] for i in range(len(nums)+1)]

        

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for val, c in count.items():
            freq[c].append(val)

        res = []

        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                k -= 1
            if k == 0:
                return res
        