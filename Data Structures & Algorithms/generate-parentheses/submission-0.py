class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # declare variables 
        result = []

        # define helper function 
        def generate(open_p:int, closed_p:int, path:str)->None:
            # base case 
            if len(path) == 2 * n:
                result.append(path[:])

            
            # generate parenthesis 
            if open_p < n:
                generate(1 + open_p, closed_p, path + "(")

            
            if closed_p < open_p:
                generate(open_p, closed_p + 1, path + ")")

        # call helper function 
        generate(0, 0, "")

        return result


        