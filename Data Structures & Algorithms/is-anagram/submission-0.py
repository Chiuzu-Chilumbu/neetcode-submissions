from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # declare variables 
        s_freq = Counter(s)
        t_freq = Counter(t)

        return s_freq == t_freq