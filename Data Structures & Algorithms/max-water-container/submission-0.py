# Optimal - maximize width first
'''
2 pointers method
1. create area var.
2. start at either ends
3. calculate area --> update area
4. whichever has the smaller height, update height

'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            
            if (heights[l] < heights[r]):
                l += 1
            elif (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
        
        return res