# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         # Create empty hash map
#         # Iterate through each element. Find target - element.
#         # If that value exists in the map, indexes of both

#         hashMap = {}

#         for index, val in enumerate(nums):
#             diff = target - val
            
#             if diff in hashMap:
#                 return [hashMap[diff], index]
            
#             hashMap[val] = index


# create a empty hashMap
# for each value in nums
    # find the diff = target - value
    # search in the hashMap if the diff exists
        # if yes
            # return [hashMap[diff], value]
        # else append the val and index.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevNum = {}

        for i, num in enumerate(nums):
            search = target - num
            if (search in prevNum):
                return [prevNum.get(search), i]
            prevNum[num] = i
        
        
