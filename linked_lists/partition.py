# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater
# than or equal to x. If x is contained within the list, the values
# of x only need to be after the elements less x (see below).
# The partition element x can appear anywhere in the "right partition";
# it does not need to appear between the left and right partitions.


# Node class to create individual nodes for the linked list
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# LinkedList class to create and manipulate the linked list
class LinkedList:
  def __init__(self):
    self.head = None

  # Method to append elements to the linked list
  def append(self, elements):
    for element in elements:
      new_node = Node(element)
      if not self.head:
        self.head = new_node
      else:
        prev_node = self.head
        while prev_node.next:
          prev_node = prev_node.next
        prev_node.next = new_node

  # Method to display the linked list
  def display(self, head):
    curr_node = head

    while curr_node:
      print(curr_node.data, end=" -> ")
      curr_node = curr_node.next
    print("None")

# Solution class containing the method to partition the linked list
class Solution:
  def partition(self, head, x):
    # Initializing pointers for left and right partitions
    left_head, left_tail = None, None
    right_head, right_tail = None, None

    # Traversing through the original linked list
    curr_node = head

    while curr_node:
      # If the value is less than x, add to the left partition
      if curr_node.data < x:
        if not left_head:
          left_head = curr_node
          left_tail = left_head
        else:
          left_tail.next = curr_node
          left_tail = left_tail.next

      # If the value is greater than or equal to x, add to the right partition
      else:
        if not right_head:
          right_head = curr_node
          right_tail = right_head
        else:
          right_tail.next = curr_node
          right_tail = right_tail.next

      # Move to the next node
      curr_node = curr_node.next

    # Ensuring the end of the right partition points to None to avoid cycles
    if right_tail:
      right_tail.next = None
    # If there are elements in the left partition, connect it to the right partition
    if left_tail:
      left_tail.next = right_head
      return left_head

    # If there are no elements in the left partition, return the right partition
    return right_head
