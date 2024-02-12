from stacks_and_queues.stack_min import MinStack

stack = MinStack()

stack.push(3)
stack.push(5)
stack.push(2)

print("Current minimum:", stack.min())  # Output: 2

stack.pop()

print("Current minimum:", stack.min())  # Output: 3