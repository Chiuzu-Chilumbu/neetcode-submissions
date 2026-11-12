from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # handle edge cases
        n = len(nums)

        if n == 0 or k == 0:
            return []

        if k == 1:
            return nums[:] # each element is it's own max window

        # declare variables 
        queue = deque() # will store inidices
        result = []

        # Build initial window
        for i in range(k):
            # handle removing max number
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            # otherwise
            queue.append(i)
        
        result.append(nums[queue[0]])

        # slide the window 
        for i in range(k, n):
            # remove indices that are out of this window
            if queue and queue[0] == i - k:
                queue.popleft()

            # insert current index
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            # the frin is the max
            result.append(nums[queue[0]])

        return result

        







