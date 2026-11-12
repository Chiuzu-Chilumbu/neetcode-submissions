class Solution:
    def encode(self, strs: List[str]) -> str:
        # declare variables
        encoded_str = ""
        # iterate through strs
        for s in strs:
            # Append the length of the string, 
            # a delimiter and the string itself
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # declare variables
        decoded = []
        i = 0

        # we iteraate while i is less than s
        while i < len(s):
            # Find the delimeter to get the length
            j = i
            while s[j] != '#':
                # increment j
                j += 1

            # Extract the length of string
            str_length = int(s[i:j])
            # Move j past the delimeter and then read 'length' characters
            decoded.append(s[j + 1 : j + 1 + str_length])
            # update i to the begging of the next encoded string
            i = j + 1 + str_length

        return decoded




