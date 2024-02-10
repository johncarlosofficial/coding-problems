from linked_lists.intersection import ListNode, Solution

# Creating instances of ListNode
# Linked List 1: 1 -> 2 -> 3 -> 4
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

# Linked List 2: 5 -> 6 -> 7
head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(7)

# Making the intersection
# Setting the last node of the second list to point to the second node of the first list
head2.next.next.next = head1.next

# Creating a Solution instance
solution = Solution()

# Finding the intersection
intersection_node = solution.intersection(head1, head2)

# Printing the value of the intersection node if it exists
if intersection_node:
  print("Intersection node value:", intersection_node.val)
else:
  print("No intersection found.")
