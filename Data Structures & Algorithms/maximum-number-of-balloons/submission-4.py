'''
b = 1
a = 1 
l = 2
o = 2
n = 1
'''

from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = defaultdict(int)
        for c in text:
            if c in "balon":
                chars[c] += 1
            
        chars["l"] = chars["l"] // 2
        chars["o"] = chars["o"] // 2

        return min(chars.values())
