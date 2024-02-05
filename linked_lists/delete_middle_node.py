# Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not 
# necessarily the exact middle) of a singly linked list, 
# given only access to that node.

# a -> b -> c -> d -> e -> f

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

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

  def display(self, head):
    curr_node = head

    while curr_node:
      print(curr_node.value)
      curr_node = curr_node.next

class Solution:
  def delete_middle_node(self, node):
    if node is None or node.next is None:
        # Cannot delete if the node is None or the last node
        return

    # Copy the value of the next node to the current node
    node.value = node.next.value

    # Remove the next node
    node.next = node.next.next