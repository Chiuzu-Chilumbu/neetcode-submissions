from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare variables 
        store = defaultdict(list)

        # iterate through strs
        for word in strs:
            # create freq list 
            freq = [0] * 26
            # search letters
            for char in word:
                # fill in freq list 
                freq[ord(char) - ord('a')] += 1

            # convert freq to tuple to use as key
            key = tuple(freq)
            store[key].append(word)

        return [values for values in store.values()]



