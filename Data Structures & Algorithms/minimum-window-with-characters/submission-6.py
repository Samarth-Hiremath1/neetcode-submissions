'''
edge case: if t = "" --> return ""

intialize:
    counts of T hashmap,
    window hashmap

    res = [-1, -1]
    resLen = float('infinity')
    have = 0
    need = len(countT)

    
l = 0
for every r:
    append to window hashmap

    if r in countT AND r window count == r countT count:
        have += 1
    
    while have == need:
        update the result
        remove from left of window
        update l += 1

if len != inf:
    return s[l:r+1]

else:
    return ""

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have, need = 0, len(countT)

        res, resLen = [-1, -1], float('infinity')

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                # update result
                if((r-l+1) < resLen):
                    res = [l, r]
                    resLen = (r-l+1)
                
                # pop from left
                window[s[l]] -= 1
                if (s[l] in countT) and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        if (resLen == float("infinity")):
            return ""
        else:
            l, r = res
            return s[l:r+1]
                
        