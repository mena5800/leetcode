class MinStack:

    def __init__(self):
        self.topindex = -1
        self.elements = []
        self.min = []
        
        

    def push(self, val: int) -> None:
        self.elements.append(val)
        self.topindex +=1
        if len(self.elements) ==1:
            self.min.append(val)
        else:
            if self.min[-1] >= val:
                self.min.append(val)
        
        
        
    def pop(self) -> None:
        if len(self.elements):
            last_one = self.elements.pop()
            if last_one == self.min[-1]:
                self.min.pop()
            self.topindex -=1

        

    def top(self) -> int:
        return self.elements[self.topindex]
        

    def getMin(self) -> int:
        return self.min[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()