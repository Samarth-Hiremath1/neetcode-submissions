
from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        '''
        countText = Counter(text)
        countBalloon = Counter("balloon")

        res = float("inf")
        for c in countBalloon:
            res = min(res, countText[c] // countBalloon[c])
        
        return res
        '''

        mp = defaultdict(int)
        for c in text:
            if c in "balon":
                mp[c] += 1
        
        mp["l"] = mp["l"]//2
        mp["o"] = mp["o"]//2

        return min(mp.values())

