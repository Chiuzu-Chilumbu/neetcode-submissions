class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # declare variables
        stack = []
        result = [0] * len(temperatures)

        # Iterate through the list
        for index, temp in enumerate(temperatures):
            # while a watmer data is found, update result
            while stack and temperatures[stack[-1]] < temp:
                popped_index = stack.pop()
                result[popped_index] = index - popped_index

            else:
                stack.append(index)

        return result