'''
# edge case 1: newInterval <<< intervals
    append newInterval
    return res + intervals[i+]
# edge case 2: newInterval >>> intervals
    append interval
# edge case 3: 
    newInterval = [min, max of interval AND newInterval]

append newInterval
return res
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i, (start, end) in enumerate(intervals):
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            
            if newInterval[0] > end:
                res.append([start, end])
            
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
            
        res.append(newInterval)
        return res
