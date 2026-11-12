class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # declare variables
        k = len(s1)
        n = len(s2)

        # edge case
        if k > n:
            return False 

        
        # handle first case
        # declare needed char freq store 
        need = [0] * 26
        for char in s1:
            need[ord(char) - ord('a')] += 1

        
        # compare window 
        window = [0] * 26
        for i in range(k):
            window[ord(s2[i]) - ord('a')] += 1

        
        # check if current window and need match 
        if need == window:
            return True 

        
        # slide by window 
        for i in range(k, n):
            # remove previous char
            window[ord(s2[i - k]) - ord('a')] -= 1
            window[ord(s2[i]) - ord('a')] += 1

            # check if windows match 
            if need == window:
                return True 

        return False





