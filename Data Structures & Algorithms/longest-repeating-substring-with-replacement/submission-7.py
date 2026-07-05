'''
option 1 to find maxF: O(26)
max(count.values())

optimal option 2: O(1)
maxf = max(maxF, counts(s[r]))

more optimal because instead of checking max of whole hashmap (O(26))
we just make 1 comparison
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        count = {}
        maxF = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res

            