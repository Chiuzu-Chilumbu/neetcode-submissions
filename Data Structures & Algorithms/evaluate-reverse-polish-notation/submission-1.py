class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # declare variables 
        stack = []
        operater = {'*', '+', '-', '/'}

        # iterate through tokens 
        for char in tokens:
            # check if operater is foiund
            if char in operater:
                # we process 
                first = stack.pop()
                second = stack.pop()

                # check wich operation to perform 
                if char == '*':
                    stack.append(second * first)

                elif char == '+':
                    stack.append(second + first)

                elif char == '-':
                    stack.append(second - first)

                else:
                    stack.append(int(second / first))


            else:
                # we check if stack is empty
                stack.append(int(char))

        return stack[-1]
                    