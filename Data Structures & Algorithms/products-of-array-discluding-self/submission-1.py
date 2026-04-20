'''
1. initailize results array
2. prefix=1
3. first pass
    a. loop through each value. for each index i
        set res[i] = prefix
        prefix *= nums[i]
4. 2nd pass
    a. loop through each value right to left. for each index i
        multiple res[i] * postfix
        update postfix *= nums[i]

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res