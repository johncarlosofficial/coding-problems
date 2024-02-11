from linked_lists.loop_detection import Node, Solution

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Create circular linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

# Test
solution = Solution()
beginning_of_loop = solution.loop_detection(node1)

if beginning_of_loop:
  print("The node at the beginning of the loop is:", beginning_of_loop.value)
else:
  print("There is no loop in the linked list.")
