class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create empty hash map
        # Iterate through each element. Find target - element.
        # If that value exists in the map, indexes of both

        hashMap = {}

        for index, val in enumerate(nums):
            diff = target - val
            
            if diff in hashMap:
                return [hashMap[diff], index]
            
            hashMap[val] = index