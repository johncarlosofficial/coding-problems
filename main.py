from stacks_and_queues.queue_via_stacks import MyQueue

my_queue = MyQueue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
my_queue.push(4)
my_queue.push(5)

print(my_queue.peek())

print(my_queue.pop())
print(my_queue.pop())

print(my_queue.isEmpty())

print(my_queue.pop())
print(my_queue.pop())
print(my_queue.pop())

print(my_queue.pop())

print(my_queue.isEmpty())
