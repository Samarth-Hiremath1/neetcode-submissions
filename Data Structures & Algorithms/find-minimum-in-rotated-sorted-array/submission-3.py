class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            # If the middle element is greater than the rightmost, the min is in the right half
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        # At the end of the loop, l == r and points to the minimum element
        return nums[l]