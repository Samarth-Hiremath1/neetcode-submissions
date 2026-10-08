

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        maxL = 0
        curr = set()

        while r < len(s):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            maxL = max(maxL, len(curr))
            r += 1
        
        return maxL