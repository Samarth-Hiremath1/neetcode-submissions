'''
sliding window

track existing chars in current window
track biggest len
keep moving right pointer as long as new char 

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curr = set()
        maxL = 0
        l =0
        
        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            maxL = max(maxL, len(curr))

        return maxL
