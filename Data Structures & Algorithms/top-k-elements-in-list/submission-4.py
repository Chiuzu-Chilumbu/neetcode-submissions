import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the freq elements
        freq = Counter(nums)

        # decalre our min heap
        min_heap = []

        # iterate through nums as we update the min heap
        for num, freq in freq.items():
            # push onto the heap
            heapq.heappush(min_heap, (freq, num)) 

            # check if we exceed k elements
            if len(min_heap) > k:
                # we remove the smallest element based on freq, not number
                heapq.heappop(min_heap)

        # we return top k
        return [num for freq, num in min_heap]