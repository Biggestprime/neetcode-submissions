class MinStack:
   def __init__(self):
      self.st = []
      self.min_stack = []
   
   def push(self, val: int) -> None:
       self.st.append(val)
       if not self.min_stack or self.min_stack[-1] >= val:
          self.min_stack.append(val)
   
   def pop(self) -> int:
       if self.st[-1] == self.min_stack[-1]:
          self.min_stack.pop()
       return self.st.pop()
   
   def getMin(self) -> int:
       return self.min_stack[-1]
   
   def top(self) -> int:
       return self.st[-1]
   
"""
1 2 3 4 5

1 
 
"""