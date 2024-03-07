# Implement a MyQueue class which implements a queue using two stacks.


class MyQueue:

  def __init__(self):
    self.main_stack = []
    self.secondary_stack = []

  def push(self, item):
    self.main_stack.append(item)

  def pop(self):
    if self.secondary_stack:
      return self.secondary_stack.pop()
    elif self.main_stack:
      for _ in range(len(self.main_stack)):
        self.secondary_stack.append(self.main_stack.pop())
      return self.secondary_stack.pop()
    else:
      return None

  def peek(self):
    if self.secondary_stack:
      return self.secondary_stack[-1]
    elif self.main_stack:
      for _ in range(len(self.main_stack)):
        self.secondary_stack.append(self.main_stack.pop())
      return self.secondary_stack[-1]
    else:
      return None

  def isEmpty(self):
    if not self.main_stack and not self.secondary_stack:
      return True
    return False
