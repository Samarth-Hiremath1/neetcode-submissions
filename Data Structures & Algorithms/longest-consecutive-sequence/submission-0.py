class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Create a set of the numbers and their sequences
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            # If the left doesn't exist, meaning start of a sequence, ...
            if (n - 1) not in numSet:
                # Counter variable to check len of sequence
                length = 0
                while (n + length) in numSet:
                    length += 1
                
                # if (length > longest) longest = length
                longest = max (length, longest)
                
        return longest