import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # declare freq counter 
        freq_store = Counter(nums)

        # define min heap
        min_heap = []

        # iterate through freq
        for num, freq in freq_store.items():
            # append to heap 
            heapq.heappush(min_heap, (freq, num))
            # check if we exceed
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]

