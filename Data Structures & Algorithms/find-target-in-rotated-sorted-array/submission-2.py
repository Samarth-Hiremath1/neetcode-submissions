class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        # Binary Search
        while (l <= r):
            # index of middle
            m = (l + r) // 2
            
            # if middle == target, return middle index
            if (nums[m] == target): 
                return m
            
            # Checking if the left side is sorted (ex. [3, 4, 5, 1, 2])
            if (nums[l] <= nums[m]):    
                # Checks if target is outside left half
                if (target > nums[m] or target < nums[l]): 
                    l = m + 1
                # If it's inside left half
                else:   
                    r = m - 1
            
            # Else, right side of array is sorted (ex. [5, 1, 2, 3, 4])
            else:
                # If target outside right sorted half
                if (target < nums[m] or target > nums[r]):
                    r = m - 1
                # else target in right sorted half
                else:
                    l = m + 1

        return -1
            
