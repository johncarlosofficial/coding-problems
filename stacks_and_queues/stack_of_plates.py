# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack
# exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
# SetOfStacks should be composed of several stacks and should create a new stack once
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
# behave identically to a single stack (that is, pop() should return the same values
# as it would if there were just a single stack). FOLLOW UP: Implement a function
# popAt(int index) which performs a pop operation on a specific sub-stack.


class SetOfStacks:

  def __init__(self, limit=3):
    self.limit = limit
    self.stacks = [[]]

  def push(self, item):
    if len(self.stacks[-1]) < self.limit:
      return self.stacks[-1].append(item)
    else:
      return self.stacks.append([item])

  def pop(self):
    popped = self.stacks[-1].pop()
    if len(self.stacks[-1]) == 0:
      self.stacks.pop()
    return popped

  def popAt(self, position):
    if position < 0 or position > len(self.stacks):
      return None

    popped = self.stacks[position].pop()

    if len(self.stacks[position]) == 0:
      del self.stacks[position]

    return popped
