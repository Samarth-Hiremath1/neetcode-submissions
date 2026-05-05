class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while (l <= r):
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # if mid is in left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    # search right side
                    l = mid + 1
                else:
                    # search left side
                    r = mid - 1

            # if mid is in right sorted portion                
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    # target is greater than mid value or 
                    # smaller than right value
                    l = mid + 1
            
        return -1
                