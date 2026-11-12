from collections import defaultdict, Counter 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Seclare variables 
        store = defaultdict(list)

        # iterate theough words
        for word in strs:
            # obtain letter frequency
            freq = Counter(word)
            key = tuple(sorted(freq.items()))

            # directly append the word to the list 
            store[key].append(word)

        return list(store.values())