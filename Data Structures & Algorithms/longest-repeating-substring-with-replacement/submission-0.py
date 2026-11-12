class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # declare variabels 
        ans = 0
        left = 0
        max_count = 0
        char_count = [0] * 26


        # iterate through string
        for right, char in enumerate(s):
            # check if current value
            index = ord(char) - ord('A')
            char_count[index] += 1
            max_count = max(max_count, char_count[index])

            # If we need more than k replacements, shrink window
            if (right - left + 1) - max_count > k:
                char_count[ord(s[left]) - ord('A')] -= 1
                left += 1 

            ans = max(ans, right - left + 1)

        return ans


