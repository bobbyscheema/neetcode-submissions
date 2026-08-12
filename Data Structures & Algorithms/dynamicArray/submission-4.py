class DynamicArray:
    

    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("Array cannot be of negative capacity")

        self.capacity = capacity
        self.size = 0
        self.data = [0] * capacity 


    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.data[self.size] = n
        self.size += 1

    def popback(self) -> int:
        removed = self.data[self.size - 1]
        self.data[self.size - 1] = 0
        self.size -= 1
        return removed

    def resize(self) -> None:
        self.capacity *= 2
        copy_data = [0] * self.capacity
        
        for i in range(len(self.data)):
            copy_data[i] = self.data[i]
        self.data = copy_data

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
