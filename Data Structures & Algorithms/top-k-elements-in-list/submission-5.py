# BF:
'''
1. count the freqs via hashmap
2. sort by freq in ascending order
3. create an empty result list
4. pop from the end of the sorted list + add to result 
list until result list reaches size k
5. return result list

time: O(nlogn)
space: O(n)
'''

# Heap:
'''
1. freq. hashmap
2. empty min-heap
3. for each # in freq. map: push it to the heap
4. if the size of the heap > than k, pop to remove the smallest frequency
5. iterate thru the entire numbers list
6. pop all elements from the heap, and add them to a results list

time: O(nlogk)
space: O(n+k)
'''

# Best Solution: Modified bucket sort
'''
1. frequency hashmap
2. create an array, where indexes represent the frequency of the values
    [[], [3], [2, 4], [1]]
3. pop from the end of this list until you reach k elements

'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, freq in count.items():
            frequency[freq].append(num)

        results = []
        for i in range(len(frequency) - 1, 0 , -1):
            for num in frequency[i]:
                results.append(num)
                if(len(results) == k):
                    return results
