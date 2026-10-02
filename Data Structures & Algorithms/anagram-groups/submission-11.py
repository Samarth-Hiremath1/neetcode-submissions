'''
1. get counts of each word into a hashmap
2. convert counts to freq_count via: (1, 2,3, ) : ["word1", "word2"]
3. return the values from the freq hashMap
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())
