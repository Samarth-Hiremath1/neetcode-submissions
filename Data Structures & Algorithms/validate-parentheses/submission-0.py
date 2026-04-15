# Use a stack LIFO
# Initialize a hashMap matching closing to opening bc opening needs to show up first

# For every char
# check if its a closing barcket found in hashmap, 
    #if not, append to stack and continue
# check if stack is empty  and if it doesnt match
    # if yes, return false
    # if not, it is valid and pop the previous element

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        matches = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # Checks if its opening backet
            if c not in matches:
                stack.append(c)
                continue
            
            # Checks if its not valid
            if not stack or stack[-1] != matches[c]:
                return False
            
            stack.pop()
        
        return not stack
            
