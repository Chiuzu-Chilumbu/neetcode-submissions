import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # obtain freq 
        freq_counter = Counter(nums)

        # declare heap 
        min_heap = []

        # store values in heap 
        for num, freq in freq_counter.items():
            # push onto heap 
            heapq.heappush(min_heap, (freq, num))

            # check if we exceed k
            if len(min_heap) > k:
                # we pop
                heapq.heappop(min_heap)

        # we return top k
        return [num for freq, num in min_heap]



