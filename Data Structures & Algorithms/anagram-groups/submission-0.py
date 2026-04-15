# hashMap/defaultdict(to not check if key exists) of character lengths / word

# for each word
    # create an array to count the # of occurances for each char
    # for each char
        # add  1 go the arr count (ord[char] - ord("a")) 

    # append word to hashMap using key tuple(arr)

# return hashMap.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(word)

        return result.values()
        
        
        
        

            
        