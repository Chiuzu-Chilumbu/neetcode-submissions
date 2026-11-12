class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # declare variables
        ans = 0
        left = 0
        max_count = 0
        letter_freq = [0] * 26

        for right, char in enumerate(s):
            # obtain index
            index = ord(char) - ord('A')
            letter_freq[index] += 1
            # obtain max count 
            max_count = max(max_count, letter_freq[index])

            # if we need more than k replacements shrink window
            if (right - left + 1) - max_count > k:
                letter_freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
