'''
- cant start with a closed parentheses
- order needs to be correct
- once match happends, can remove the last added pair 
    -> use stack, use closeToOpen
- stack has to be empty in the end

'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                # if stack isn't empty AND last one matches open parentheses
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True