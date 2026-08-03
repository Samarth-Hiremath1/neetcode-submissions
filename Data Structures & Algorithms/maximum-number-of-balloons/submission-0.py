

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        countText = Counter(text)
        countBalloon = Counter("balloon")

        res = float("inf")
        for c in countBalloon:
            res = min(res, countText[c] // countBalloon[c])
        
        return res