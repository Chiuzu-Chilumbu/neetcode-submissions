from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare variables
        groups = defaultdict(list)

        # iterate through strs list 
        for string in strs:
            # create the freq array
            freq = [0] * 26
            # iterate through character
            for char in string:
                # build freq array 
                freq[ord(char) - ord('a')] += 1

            # append string to groups 
            groups[tuple(freq)].append(string)

        return [lists for lists in groups.values()]