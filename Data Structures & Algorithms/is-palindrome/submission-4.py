class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while (left < right):
            while left < right and (self.alphaNum(s[left]) != True):
                left += 1
            
            while right > left and (self.alphaNum(s[right]) != True):
                right -= 1

            if (s[left].lower() != s[right].lower()):
                return False

            left += 1
            right -= 1

        return True


    def alphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))