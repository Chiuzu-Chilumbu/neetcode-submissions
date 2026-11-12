class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # declare variables
        k = len(s1)
        n = len(s2)

        # edge case 
        if k > n:
            return False

        # 1. Build frequency of s1
        need = [0] * 26
        for char in s1:
            need[ord(char) - ord('a')] += 1

        # 2. Build first window including window char freq
        window = [0] * 26
        for i in range(k):
            window[ord(s2[i]) - ord('a')] += 1

        # check initial window 
        if window == need:
            return True 

        
        # 3. slide window over the rest of s2
        for i in range(k, n):
            # add s2[i], remove s[i - k]
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - k]) - ord('a')] -= 1

            if window == need:
                return True 

        # 4 No match found
        return False
