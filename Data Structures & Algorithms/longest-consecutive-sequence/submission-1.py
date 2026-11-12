class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # declare variables 
        longest = 0
        num_set = set(nums)


        # iterate through the nums
        for num in nums:
            # check if this is starting number 
            if num - 1 not in num_set:
                # start streak 
                current_num = num
                current_streak = 1

                # we update streak whilst next number in set
                while current_num + 1 in num_set:
                    current_streak += 1
                    current_num = current_num + 1

                # update the longest streak 
                longest = max(current_streak, longest)

        return longest