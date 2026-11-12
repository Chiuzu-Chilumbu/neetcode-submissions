class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # declare variables 
        result = []
        n = len(nums)

        # sort numbers
        nums.sort()

        # traverse the list 
        for i in range(n - 2):
            # skip duplicates 
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            # declare pointers 
            left, right = i + 1, n - 1

            # close pointers 
            while left < right:
                # obtain first triplet
                current = nums[i] + nums[left] + nums[right]

                # check if sum eq 0
                if current == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # move to next value and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1


                    # move pointers
                    left += 1
                    right -= 1

                
                # otherwise :
                elif current > 0:
                    right -= 1

                else:
                    left += 1
        
        return result






