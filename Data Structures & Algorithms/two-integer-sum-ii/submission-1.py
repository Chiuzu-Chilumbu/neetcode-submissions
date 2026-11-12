class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # declare pointers 
        left, right = 0, len(numbers) - 1

        # close pointers 
        while left < right:
            # obtain current sum 
            current_sum = numbers[left] + numbers[right]

            # check if found 
            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum > target:
                right -= 1

            else:
                left += 1

        return [-1, -1]