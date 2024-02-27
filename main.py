from stacks_and_queues.three_in_one import MyStack

my_stack = MyStack(3)
my_stack.push(0, 1)
my_stack.push(0, 2)
my_stack.push(1, 2)
my_stack.push(1, 3)
my_stack.push(2, 3)
my_stack.pop(1)
my_stack.pop(1)

print(my_stack.array)

print(my_stack.peek(0), my_stack.isEmpty(1))
