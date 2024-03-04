from stacks_and_queues.stack_of_plates import SetOfStacks

s = SetOfStacks(1)
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.popAt(0))
print(s.popAt(2))


