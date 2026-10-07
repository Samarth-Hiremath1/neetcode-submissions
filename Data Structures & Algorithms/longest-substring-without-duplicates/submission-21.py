'''
2 pointer approach

track currSet
track maxL
keep moving r until r in currSet
    keep popping from left


'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currSet = set()
        maxL = 0

        l,r = 0, 0

        while r < len(s):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1
            currSet.add(s[r])
            maxL = max(maxL, len(currSet))

            r += 1
        
        return maxL
