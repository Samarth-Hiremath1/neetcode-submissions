class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Sol 1:
        1. extract only alphanumeric functions
        2. check if it is the same as the reversed version

        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        '''

        '''
        Sol 2:
        1. create helper function for alphaNum
        2. 2 pointers: l, r, check every alphaNum char
        '''

        l, r = 0, len(s) - 1

        while l < r:
            while (l < r) and (self.alphaNum(s[l]) == False):
                l += 1 
            while (r > l) and (self.alphaNum(s[r]) == False):
                r -= 1
            
            if(s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
        return True


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
         ord('a') <= ord(c) <= ord('z') or
         ord('0') <= ord(c) <= ord('9'))
