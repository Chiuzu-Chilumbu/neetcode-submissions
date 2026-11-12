class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # declare variables 
        k = len(s1)
        n = len(s2)

        # edge case
        if k > n:
            return False 

        # 1. Build frequency of s1
        need = [0] * 26
        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        # 2. Build initial window for first k chars or s2
        window = [0] * 26
        for i in range(k):
            window[ord(s2[i]) - ord('a')] += 1

        # check initial window
        if window == need:
            return True

        
        # 4) slide window over the rest of s2
        for i in range(k, n):
            # add s2[i], remove s2[i - k]
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - k]) - ord('a')] -= 1

            if window == need:
                return True 

        # 5) no match found
        return False




