class MyQueue:

    def __init__(self):
        self.elements = []
        
        

    def push(self, x: int) -> None:
        self.elements.append(x)
        

    def pop(self) -> int:
        pop_element = self.elements.pop(0)
        return pop_element

    def peek(self) -> int:
        return self.elements[0]
        

    def empty(self) -> bool:
        if len(self.elements)>0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()