class Solution:

    def encode(self, strs: List[str]) -> str:
        # declare variables 
        encoded = ""
        # iterate through strs
        for word in strs:
            # add len(string) , delimeter and string to  encoded
            encoded += str(len(word)) + '#' + word
        
        return encoded


    def decode(self, s: str) -> List[str]:
        # declare variables 
        i = 0
        decoded = []

        # traverse until end 
        while i < len(s):
            # decalre variable to traverse word 
            j = i
            # search delimeter 
            while s[j] != '#':
                j += 1

            # if delimeter is found we obtain string [i:j]
            word_len = int(s[i:j]) 
            decoded.append(s[j + 1: j + 1 + word_len])

            # update i and begin
            i = j + 1 + word_len

        return decoded

        



