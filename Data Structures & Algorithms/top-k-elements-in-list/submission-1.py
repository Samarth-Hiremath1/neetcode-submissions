# Create empty hash map [num : # of times displayed]
# Create a max heap with tuples (-freq, value)
# Pop k times and append into an array
# Return array


# Time Complexity: O(n + klog(n))
# Heap Construction:
# Creating the list of tuples: O(n)
# Heapifying the list: O(n)
# Extracting k Elements: O(k log n), because each extraction operation from a heap of size n takes O(log n) time, and we do this k times.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize the frequency dictionary
        # hashMap = defaultdict(int)
        hashMap = {}

        # Count the frequency of each element
        for num in nums:
            # hashMap[num] += 1
            hashMap[num] = hashMap.get(num, 0) + 1

        # Create a list of tuples with negative frequencies and the corresponding numbers
        heap = []
        for num, freq in hashMap.items():
            heap.append((-freq, num))

        # Transform the list into a heap
        heapq.heapify(heap)

        # Extract the top k elements from the heap
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result