from collections import Counter 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if len(t) > len(s):
            return ""

        
        # declare variables 
        need = Counter(t)
        window = {}
        required = len(need)
        formed = 0

        # pointers
        left = 0
        ans = (float("inf"), None, None) # length, left, right

        # expand the window
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            # Contract while valid
            while formed == required:
                # update answer 
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)

                # remove from left 
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]






