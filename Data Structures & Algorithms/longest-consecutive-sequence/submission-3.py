# Optimal
'''
1. convert arr to set
2. iterate through every num
    a. if num-1 doesn't exist (then it's start of a sequence):
        i. sequence length = 0
        ii. while (n+length)

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longestLen = 0

        for n in numSet:
            # check if its the start of a sequence
            if(n-1) not in numSet:
                length = 1
                while(n+length) in numSet:
                    length += 1
                longestLen = max(length, longestLen)

        return longestLen