'''
Binary search
l, m, r
if m >= nums[l]:
    search right (m-> l)
else:
    search left (bc the pivot would be somewhere left)

[7, 8, 9, 1, 2, 3, 4, 5, 6]

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            # if subarray is sorted:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            # find mid
            m = (l + r) // 2
            res = min(res, nums[m])

            # check if mid is part of left or right sorted portion
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m 
        
        return res