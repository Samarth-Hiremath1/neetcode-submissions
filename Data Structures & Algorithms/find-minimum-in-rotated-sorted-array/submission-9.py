'''
modified binary search via 2 pointers

while l <= r:
    check if we are in a sorted array : res = left, break
    
    l, r, m = (l+r)//2

    if m >= l ([5, 6, 7, 1, 2, 3, 4, 50]):
        search right l = m+1
    else:
        search left r = m-1
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]

        l = 0
        r = len(nums)-1
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if (nums[m] >= nums[l]):
                l = m+1
            else:
                r = m-1
        
        return res




