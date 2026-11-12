class Solution:
    def isValid(self, s: str) -> bool:
        # declare variables 
        stack = []
        parenthesis = {"]": "[", "}": "{", ")":"("}

        # iterate through s
        for char in s:
            # check if closing is found 
            if char in parenthesis.keys():
                # check if we can pop
                if stack and stack[-1] == parenthesis[char]:
                    stack.pop() 

                else:
                    return False 

            else:
                # it is open so we append to stack
                stack.append(char)

        return stack == []