'''
organize every char into:
26 chars, 0-25, representing a-z
make that a key : value
    values become the actual word
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        maps = defaultdict(list)

        for string in strs:
            cnt = [0]*26
            for s in string:
                cnt[ord(s) - ord('a')] += 1
            maps[tuple(cnt)].append(string)
        
        return list(maps.values())