# Use binary search bc O(log n)

# initialize length, l, r pointers
# while l and right pointers dont cross
#       find the middle
#       if middle > right, it means the minimum is in the right sorted portion
#               update l to be at middle
#       else, it means min is in left sorted portion
#               update r to be at middle and continue w binary search
#  return new left

class Solution:
    def findMin(self, nums: List[int]) -> int:
         n = len(nums)
         l = 0
         r = n - 1

         while (l < r):
            m = (l + r) // 2
            if (nums[m] > nums[r]):
                l = m + 1
            else:
                r = m
        
         return nums[l]