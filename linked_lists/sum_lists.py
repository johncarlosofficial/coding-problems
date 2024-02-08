# You have two numbers represented by a linked list, where each node
# contains a single digit. The digits are stored in reverse order, such that
# the 1's digit is at the head of the list. Write a function that adds two
# numbers and returns the sum as a linked list.

# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.


class Node:

  def __init__(self, val):
    self.val = val
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def append(self, elements):
    for i in range(len(elements)):
      new_node = Node(elements[i])
      if not self.head:
        self.head = new_node
      else:
        curr_node = self.head
        while curr_node.next:
          curr_node = curr_node.next
        curr_node.next = new_node

  # NEW SOLUTION: if the linked lists are not reversed, reverse them.
  def reverse_list(self, head):
    if not head.next:
      return head

    prev_node = None
    curr_node = head

    while curr_node:
      next_node = curr_node.next
      curr_node.next = prev_node
      prev_node = curr_node
      curr_node = next_node

    return prev_node

  def display(self):
    curr_node = self.head
    while curr_node:
      print(curr_node.val, end=" -> ")
      curr_node = curr_node.next
    print("None")


class Solution:

  def __init__(self):
    self.head = None

  def add_lists(self, head1, head2):
    curr1 = head1
    curr2 = head2
    carry = 0
    dummy_node = Node(0)
    curr_node = dummy_node

    while curr1 or curr2 or carry:
      val1 = curr1.val if curr1 else 0
      val2 = curr2.val if curr2 else 0

      s = val1 + val2 + carry

      remainer = s % 10
      carry = s // 10

      curr_node.next = Node(remainer)

      curr_node = curr_node.next
      curr1 = curr1.next if curr1 else None
      curr2 = curr2.next if curr2 else None

    return dummy_node.next
