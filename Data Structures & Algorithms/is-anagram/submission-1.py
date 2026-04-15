# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
#         if (len(s) != len(t)):
#             return False

#         mapS = {}
#         mapT = {}

#         for i in range(len(s)):
#             mapS[s[i]] = 1 + mapS.get(s[i], 0)
#             mapT[t[i]] = 1 + mapT.get(t[i], 0)
        
#         for val in mapS:
#             if (mapS[val] != mapT.get(val, 0)):
#                 return False
        
#         return True


# Create a empty hashMap for s
# for each char, add the count
# if the count s != count t
    # return false
# return true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        countS = {} # Empty hashmaps of either one
        countT = {} # Empty hashmaps of either one

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return (countS == countT)
        
