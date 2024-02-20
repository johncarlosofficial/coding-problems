# Write a program to sort a stack such that the smallest items are on the top. 
# You can use an additional temporary stack, but you may not copy the elements into any 
# other data structure (such as an array). 
# The stack supports the following operations: push, pop, peek, and isEmpty.

class Solution:
  def sort_stack(self, stack):
    temp_stack = []
    
    while len(stack) != 0:
      stack_popped = stack.pop()
      while len(temp_stack) != 0 and temp_stack[-1] > stack_popped:
        stack.append(temp_stack.pop())
      temp_stack.append(stack_popped)

    while len(temp_stack) != 0:
      stack.append(temp_stack.pop())

    return stack