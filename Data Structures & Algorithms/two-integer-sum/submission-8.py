class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevNums = {} # num : index

        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevNums:
                return[prevNums[diff], i]
            prevNums[n] = i
        return
