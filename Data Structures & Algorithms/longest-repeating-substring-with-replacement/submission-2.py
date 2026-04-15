# Have a hasmap that stores the number of occurances of 
#     each character in the current window

# Initialize a variable to result the result

# left pointer = start
# right pointer increases with a for loop

# add each character to the count hashmap to maintain accurate count

# if (len of window - most occuring char) > k (represents replaceable chars)
#     then invalid

#     if invalid, remove the count of the left-most char from count hashmap
#     move up left pointer

# else, check if window size is larger than current max length

# return length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}

        result = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while ((r-l+1) - (max(count.values())) > k):
                count[s[l]] -= 1
                l +=1 

            result = max(result, r - l + 1)
        
        return result
        