class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""

        # hashmap for target and for current window
        countT, window = {}, {}

        # initialize countT hashmap (hashmap 
        # containing the target chars + how many of each char)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        res, resLen = [-1, -1], float("infinity")
        
        
        l = 0
        for r in range(len(s)):
            # update chars in window
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # check window and target
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # update result
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                
                # pop from left of window and slide window
                window[s[l]] -= 1
                # update have/need count
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""