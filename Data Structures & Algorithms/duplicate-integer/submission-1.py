class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         values = set()
         for i in range(len(nums)):
            if (nums[i] in values):
                return True
            values.add(nums[i])
            
         return False