class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # declare variables
        longest = 0
        num_set = set(nums)

        # iterate through nums to find the starting integer
        for num in nums:
            # check if the first number in sequence is found
            if num - 1 not in num_set:
                current_streak = 1
                current_num = num

                # check if next number exists 
                while current_num + 1 in num_set:
                    current_streak += 1
                    current_num = current_num + 1

                # update longest streak 
                longest = max(current_streak, longest)

        return longest


