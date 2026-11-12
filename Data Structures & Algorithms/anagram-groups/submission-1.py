class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare variables 
        store = defaultdict(list)

        # Iterate through list
        for word in strs:
            # build letter freq
            freq = [0] * 26
            # iterate through characters
            for char in word:
                # build frequency map
                freq[ord(char) - ord('a')] += 1

            # use freq as key
            key = tuple(freq)
            store[key].append(word)

        return list(store.values())