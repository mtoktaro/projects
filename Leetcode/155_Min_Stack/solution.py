class MinStack:

    def __init__(self):
        self.st = []
        return None
        
    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None:
            self.st.append((val, val))
        else:
            self.st.append((val, min(val, self.st[-1][1])))
      
        return None
        
    def pop(self) -> None:
        self.st.pop()
        return None
        
    def top(self) -> int:
        
        if len(self.st) > 0:
            return self.st[-1][0]
        else:
            return None
    
    def getMin(self) -> int:
        if len(self.st) > 0:
            return self.st[-1][1]
        else:
            return None
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()