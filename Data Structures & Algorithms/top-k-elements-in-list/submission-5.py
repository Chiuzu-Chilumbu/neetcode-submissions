import heapq
from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store char num count in Counter
        freq = Counter(nums)
        # define heap
        heap = []

        # iterate through string 
        for num, count in freq.items():
            # push onto heap 
            heapq.heappush(heap, (count, num))
            # check if length is exceeded
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]
