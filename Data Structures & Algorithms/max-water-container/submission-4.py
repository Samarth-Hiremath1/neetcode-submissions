class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        largest = 0

        while l < r:
            # calculate area and largest
            area = (r-l) * min(heights[l],heights[r])
            largest = max(largest, area)

            # udpdate pointers
            if heights[l] < heights[r]:
                l += 1
            #elif heights[l] > heights[r]:
            #    r -= 1
            
            else:
                r -= 1

        return largest

