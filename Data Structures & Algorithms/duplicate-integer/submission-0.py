from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # decalre variables 
        freq_count = Counter(nums)

        # iterate through frequencies
        for key, value in freq_count.items():
            if value > 1:
                return True

        return False