class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # BF / Manual
        '''
        create a new empty string
        append all alphanumeric 
        check if it is the same being read back and forth
        '''

        # newStr = ""

        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        
        # return (newStr == newStr[::-1])


        # Optimal - 2 pointers

        l, r = 0, len(s)-1

        while l < r:
            # if it didn't cross yet AND it's not an alphaNum
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l+1, r-1

        return True

         
    # Use ascii values to check if it is a alphanumeric value
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))