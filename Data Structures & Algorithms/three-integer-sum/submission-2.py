class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # declare variables
        result = []
        n = len(nums)

        # sort nums in ascending order
        nums.sort()

        # begin iterating through nums
        for i in range(n - 2):
            # skip duplicates while not at first index
            if i > 0 and nums[i] == nums[i - 1]:
                continue


            # declare pointers
            left, right = i + 1, n - 1

            # close pointers
            while left < right:
                # obtain current sum
                current_sum = nums[i] + nums[left] + nums[right]
                # check if current sum eq 0
                if current_sum == 0:
                    # store triples in results array
                    result.append([nums[i], nums[left], nums[right]])

                    # move pointers to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # update pointers
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1

                else:
                    right -= 1

        return result