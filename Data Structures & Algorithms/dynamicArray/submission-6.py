class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity < 0:
            return ValueError
        self.capacity = capacity
        self.size = 0
        self.items = [0] * capacity


    def get(self, i: int) -> int:
        return self.items[i]


    def set(self, i: int, n: int) -> None:
        self.items[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.items[self.size] = n
        self.size += 1


    def popback(self) -> int:
        value = self.items[self.size - 1]
        self.items[self.size - 1] = 0
        self.size -= 1
        return value

    def resize(self) -> None:
        self.capacity *= 2
        new_list = [0] * self.capacity

        for i in range(len(self.items)):
            new_list[i] = self.items[i]
        
        self.items = new_list

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity