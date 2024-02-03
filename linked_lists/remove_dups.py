# Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?


class Node:
  def __init__(self, value):
    self.next = None
    self.value = value


class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    else:
      prev_node = self.head
      while prev_node.next:
        prev_node = prev_node.next
      prev_node.next = new_node

  def display(self, head):
    curr_node = head
    while curr_node:
      print(curr_node.value, end=" ")
      curr_node = curr_node.next


class Solution:
  def remove_dups(self, head):
    # Use a set to keep track of unique values encountered
    dictionary = set()
    curr_node = head
    prev_node = None

    # Traverse the linked list
    while curr_node:
      # If the current value is already in the set, skip this node by updating the pointers
      if curr_node.value in dictionary:
        prev_node.next = curr_node.next
      else:
        # If the value is not in the set, add it to the set and update the pointers
        dictionary.add(curr_node.value)
        prev_node = curr_node
      curr_node = curr_node.next

    return head  # Return the head of the modified linked list
