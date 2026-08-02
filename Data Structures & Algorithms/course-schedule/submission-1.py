'''
adj. list of all connections

seen = set()

def dfs(course):
    if in seen: return False
    if preReqMap == []: return True

    seen.add()
    for preReq in course:
        if dfs(preReq) == False: return False      # been see, thus loop
    seen.remove()
    preReqMap[course] = []
    return True


for every course in range(numCourses):
    if dfs(course) == False:
        return False

return True


'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReqMap = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites:
            preReqMap[course].append(preReq)
        
        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if preReqMap[course] == []:
                return True
            
            seen.add(course)
            for pre in preReqMap[course]:
                if dfs(pre) == False:
                    return False
            seen.remove(course)
            preReqMap[course] = []
            return True


        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True




