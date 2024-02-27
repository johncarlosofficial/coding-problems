# Describe how you could use a single array to implement three stacks.


class MyStack:

  def __init__(self, stack_size):
    self.stack_size = stack_size
    self.array = [None] * (3 * self.stack_size)
    self.pointers = [-1, -1, -1]

  def push(self, stack_num, value):
    if self.pointers[stack_num] < self.stack_size - 1:
      self.pointers[stack_num] += 1
      index = stack_num * self.stack_size + self.pointers[stack_num]
      self.array[index] = value
    else:
      print("Stack Overflow")

  def pop(self, stack_num):
    if self.pointers[stack_num] > -1:
      index = stack_num * self.stack_size + self.pointers[stack_num]
      self.array[index] = None
      self.pointers[stack_num] -= 1
    else:
      print("Stack Overflow")

  def peek(self, stack_num):
    index = self.pointers[stack_num]
    return self.array[index]

  def isEmpty(self, stack_num):
    return self.pointers[stack_num] < 0
