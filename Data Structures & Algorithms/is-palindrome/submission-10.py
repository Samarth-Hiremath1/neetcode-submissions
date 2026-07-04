class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Sol 1:
        1. extract only alphanumeric functions
        2. check if it is the same as the reversed version
        '''

        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]