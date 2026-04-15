# BF:
'''
1. sort all the strings
2. check which ones have the same values

O(m*nlogn)
'''

# DSA
'''
1. hashmap --> count : strings
2. return hashmaps

O(m*n*26) --> O(mn)

'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] *26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)
        
        return list(result.values())









