# BF:
'''
triple nested loops to loop through 
    all possible combinations of 3 that 
    meet the sum

remove duplicates

T: O(n^3)
S: O(1)
'''

# Optimal - 2 pointers
'''
1. sort array (handles duplicates + allows us to do 2 sum on the rest
    of the array)
2. loop through the array using index i
    a. let a=nums[i]
    b. if a>0, break


'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            
            # if the value is the same as prev. value, skip
            if (i > 0 and val == nums[i-1]):
                continue
            
            # 2 sum for the rest of the array
            l, r = i + 1, len(nums) -1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                
                if threeSum < 0:
                    l += 1

                if threeSum == 0:
                    res.append([val, nums[l], nums[r]])

                    # only need up update 1 pointer bc the 2
                    # if statements above will adjust pointers
                    # automatically
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res








