from linked_lists.sum_lists import ListNode, Solution

def print_list(node):
  while node:
      print(node.val, end=" -> ")
      node = node.next
  print("None")

# Define the linked lists
l1 = ListNode(7)
l1.next = ListNode(1)
l1.next.next = ListNode(6)

l2 = ListNode(5)
l2.next = ListNode(9)
l2.next.next = ListNode(2)

# Test the sum_lists function
solution = Solution()
result = solution.sum_lists(l1, l2)

# Print the result
print("Sum of the lists:")
print_list(result)
