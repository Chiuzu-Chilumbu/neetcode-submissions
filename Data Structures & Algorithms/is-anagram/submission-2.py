class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case 
        if len(s) != len(t):
            return False

        # since we are only using lowecase letters we can do this in constant space
        # decalre variabeles
        freq = [0] * 26

        # iterate through strings and note char counts
        for a, b in zip(s, t):
            # insert based on char order
            freq[ord(a) - ord('a')] += 1
            freq[ord(b) - ord('a')] -= 1

        return all(c == 0 for c in freq)
