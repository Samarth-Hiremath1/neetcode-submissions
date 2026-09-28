class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currChars = set()
        maxL = 0

        l=0
        
        for r in range(len(s)):
            while s[r] in currChars:
                currChars.remove(s[l])
                l+=1
            currChars.add(s[r])
            maxL = max(maxL, len(currChars))
        
        return maxL