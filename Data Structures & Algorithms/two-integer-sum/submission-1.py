class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # declare variables 
        seen = {} #key->num, value->index

        # iterate through list
        for index, num in enumerate(nums):
            # calculate the compliment 
            compliment = target - num
            # check if compliment is in seen 
            if compliment in seen:
                return [seen[compliment], index]

            seen[num] = index
