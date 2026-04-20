class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevVals = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevVals:
                return [prevVals[diff], i]
            prevVals[n] = i