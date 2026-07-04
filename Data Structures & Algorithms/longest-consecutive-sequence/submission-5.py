'''
Convert input array into a set

Check if each number is the start of a sequence 
    (check if n-1 is in set)

If yes, check if n+1 is in set, and keep continue checking

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0 
        
        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
