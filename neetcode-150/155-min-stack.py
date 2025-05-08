class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []
        
    def push(self, val: int) -> None:
        self.st.append(val)

        if not self.min_st or val <= self.min_st[-1]:
            self.min_st.append(val)
   
    def pop(self) -> None:
        val = self.st.pop()
        if val == self.min_st[-1]:
            self.min_st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.min_st[-1]