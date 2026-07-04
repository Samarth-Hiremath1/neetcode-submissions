'''
1. sort array
2. create a res = [] 
3. enumerate through every element
    2 sum with LR pointers on everything else
    l, r pointers

    if (currNum == prevNum):
        continue

    while l < r:
        threeSum = a + b + c
        if 3sum < 0:
            l += 1
        elif 3sum > 0:
            r -= 1
        else:
            res.append(a,b,c)
            l += 1
            while (l == l-1) and (l < r):
                l += 1
            

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if (i != 0) and (nums[i] == nums[i-1]):
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if (threeSum < 0):
                    l += 1
                elif (threeSum > 0):
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l-1]) and (l < r):
                        l += 1
        return res

