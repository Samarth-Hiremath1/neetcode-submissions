# nums = [-1,0,1,2,-1,-4]
# nums = [-4,-1,-1,0,1,2]

# sort the array
# output = []

# for every a and index in nums:
#     if(nums[index] == nums[index-1] and index != 0):
#         continue

#         # indexes for left and right
#         l = next index
#         r = last index

#         while (left < right):
#                 totalSum = a + l + r
#                 if ( sum > 0):
#                     reduce right

#                 if ( sum < 0 ):
#                     incrase left
                
#                 if ( sum = 0):
#                     append to the output
#                     l += 1
#                     r -= 1
#                     while (left is the same as the value before AND l < r):
#                         incrase by 1


#         return output


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output = []

        for index, a in enumerate(nums):
            if(nums[index] == nums[index-1] and index != 0):
                continue
            
            # 2Sum with pointers
            l = index + 1
            r = len(nums) - 1

            while (l < r):
                threeSum = a + nums[l] + nums[r]

                if(threeSum > 0):
                    r -= 1
                
                elif (threeSum < 0):
                    l += 1

                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while(nums[l] == nums[l-1] and l < r):
                        l += 1

        return output

