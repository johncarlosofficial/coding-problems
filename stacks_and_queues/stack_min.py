# How would you design a stack which, in addition to push and pop, 
# has a function min which returns the minimum element? 
# Push, pop, and min should all operate in O(1) time.

class MinStack:
  def __init__(self):
      self.stack = []  # main stack to store elements
      self.min_stack = []  # auxiliary stack to keep track of minimums

  def push(self, x):
      self.stack.append(x)
      if not self.min_stack or x < self.min_stack[-1]:  # if x is smaller or equal to the current minimum
          self.min_stack.append(x)

  def pop(self):
      if self.stack:
          popped = self.stack.pop()
          if popped == self.min_stack[-1]:  # if the popped element is the current minimum
              self.min_stack.pop()
          return popped
      else:
          return None  # or raise an exception for empty stack

  def min(self):
      if self.min_stack:
          return self.min_stack[-1]
      else:
          return None  # or raise an exception for empty stack
