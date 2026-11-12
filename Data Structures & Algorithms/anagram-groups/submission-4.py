from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare variables
        groups = defaultdict(list)

        # iterate through the string
        for string in strs:
            # declare freq array 
            freq = [0] * 26
            # iterate through each char
            for char in string:
                # strore freq
                freq[ord(char) - ord('a')] += 1 
            
            # store in defaultdict, it handles duplicates so no need for conditional
            groups[tuple(freq)].append(string)

        # return list of grouped anagrams
        return list(groups.values())