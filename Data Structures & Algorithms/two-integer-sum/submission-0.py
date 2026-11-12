from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # declare variables 
        store = defaultdict(int)

        # iterate through numbers
        for index, num in enumerate(nums):
            # obtain compliment 
            compliment = target - num
            # check if exists
            if compliment in store:
                return [store[compliment], index]

            else:
                store[num] = index

        return [-1, -1]