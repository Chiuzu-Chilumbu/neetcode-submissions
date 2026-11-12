class MinStack:

    def __init__(self):
        # declare stack 
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)

        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(current_min, val))

        self.stack.append(val)

        

    def pop(self) -> None:
        # check if stack are nto empty 
        self.stack.pop()
        self.min_stack.pop()

        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
