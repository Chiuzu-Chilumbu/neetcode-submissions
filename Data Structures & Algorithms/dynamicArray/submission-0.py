class DynamicArray:
    
    def __init__(self, capacity: int):
        self.last = 0
        self.capacity = capacity
        self.array = [None] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.last:
            raise IndexError("Index out of bounds")
        self.array[i] = n


    def pushback(self, n: int) -> None:
        # resize array if capacity is reached
        if self.last >= self.capacity:
            self.resize()

        self.array[self.last] = n
        self.last += 1


    def popback(self) -> int:
        if self.last == 0:
            raise IndexError("pop from empty array")

        self.last -= 1
        removed = self.array[self.last]
        self.array[self.last] = None
        return removed 


    def resize(self) -> None:
        self.capacity *= 2
        new_array = [None] * self.capacity

        for i in range(self.last):
            new_array[i] = self.array[i]
        
        self.array = new_array


    def getSize(self) -> int:
        return self.last

    
    def getCapacity(self) -> int:
        return self.capacity
