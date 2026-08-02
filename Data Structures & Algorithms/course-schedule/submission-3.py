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

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if prereqMap[course] == []:
                return True
            
            seen.add(course)
            for preReq in prereqMap[course]:
                if dfs(preReq) == False:
                    return False
            seen.remove(course)
            prereqMap[course] = []
            return True
        

        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
        