'''
adj. list mapping all courses -> prerequs via {}

seen = set()
def rec_dfs(course):
    if (course in seen): return False
    if has no preReqs : return True

    seen.add(course)
    for preReq in course:
        if dfs(preReq) == False:
            return False
    seen.remove(course)
    update preReqMap = []
    return True


for course in range(numCourses):
    if dfs(course) == False:
        return False
return True

'''

# cycles X
'''
create adj. list

seen = set()

def dfs(course):
    if course in seen: return False
    if no prereqs: return True

    seen.add(course)
    for preReq in course:
        if dfs(preReq) == False:
            return False
    seen.remove(course)
    course == remove preReqs -> []
    return True



iterate through every course:
    if dfs(course) == False --> return False
return True
'''

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReqMap = {v: [] for v in range(numCourses)}
        for u, v in prerequisites:
            preReqMap[v].append(u)
        
        seen = set()

        def dfs(course):
            if(course in seen):
                return False
            if (preReqMap[course] == []):
                return True
            
            seen.add(course)
            for preReq in preReqMap[course]:
                if dfs(preReq) == False:
                    return False
            seen.remove(course)
            preReqMap[course] = []
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
