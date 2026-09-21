class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minL = float('inf')
        l = 0
        sumS = 0

        for r in range(len(nums)):
            sumS += nums[r]

            while sumS >= target:
                minL = min(r-l+1, minL)
                sumS -= nums[l]
                l += 1
        
        if minL == float('inf'):
            return 0
        else:
            return minL
