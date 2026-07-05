'''
sliding window

hashmap to track freq

for every r:
    update freq hashmap
    calculate maxFreq (more optimal)
    check validity
        make updates
    check max length

to check valid substring: length - maxF > k ---> invalid
    update freq hashmap
    move left pointer

check max length

'''


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
        
        longest = 0
        mostF = 0

        counts = {}

        l = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            mostF = max(mostF, counts[s[r]])

            while (r-l+1) - mostF > k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)

        return longest
        