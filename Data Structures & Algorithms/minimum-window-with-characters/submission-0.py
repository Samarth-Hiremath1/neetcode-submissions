class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Edge cases (t length is empty or > than s length)
        if len(t) > len(s): return ""
        if t == "": return ""

        # Defining variables
        window = {}             # How many target char in window
        countT = {}             # How many target char in t
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        
        have = 0                # How many target we currently have
        need = len(countT)      # How many target we need

        result = [-1, -1]       # Indexes of substring
        resultLen = float("infinity")       # Length of final. Looking for smallest

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while (have == need):
                if (r - l + 1) < resultLen:     # Update results
                    result = [l, r]
                    resultLen = r - l + 1
                
                window[s[l]] -= 1               # Remove left char from window

                # If removed left char was in countT, reduce have variable
                if s[l] in countT and (window[s[l]] < countT[s[l]]):
                    have -= 1

                # update left pointer
                l += 1

        #Update result and return
        l = result[0]
        r = result[1]

        if resultLen != float("infinity"):
            return (s[l:r+1])
        
        else: return ""
                




