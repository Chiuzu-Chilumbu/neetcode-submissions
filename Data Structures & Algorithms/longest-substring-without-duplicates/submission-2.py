class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # declare varaibles 
        left = 0
        longest = 0
        unique = set()

        # traverse s
        for right in range(len(s)):
            # check if s[right] exist
            while s[right] in unique:
                unique.remove(s[left])
                left += 1

            # add to unique 
            unique.add(s[right])

            # compare longest
            longest = max(longest, right - left + 1)

        return longest