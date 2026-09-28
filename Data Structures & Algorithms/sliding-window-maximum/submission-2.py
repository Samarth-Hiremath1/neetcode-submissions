from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque()

        for i, num in enumerate(nums):
            
            # pop from right of que if new num > than latest num
            while q and nums[q[-1]] <= num:
                q.pop()
            
            q.append(i)

            # pop from left of que if out of range
            if q[0] <= i-k:
                q.popleft()
            
            if i >=k-1:
                res.append(nums[q[0]])
        return res