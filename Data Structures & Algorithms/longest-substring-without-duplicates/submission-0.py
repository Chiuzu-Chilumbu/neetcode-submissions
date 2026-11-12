class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # declare variables 
        left = 0
        unique = set()
        longest = 0

        # traverse sting 
        for right in range(len(s)):
            # obtain current longest
            # pass

            # check if s[right] in unique 
            while s[right] in unique:
                # move left pointer
                unique.remove(s[left])
                left += 1

            
            # add current right
            unique.add(s[right])

            # calculate the substring length
            longest = max(longest, right - left + 1)

        return longest