# Implement an algorithm to find the kth to last element of a singly linked list.


class Node:
  def __init__(self, data):
    self.data = data
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
    arr = []
    prev_node = head
    while prev_node.next:
      arr.append(prev_node.data)
      prev_node = prev_node.next
    arr.append(prev_node.data)

    return arr


# Class implementing the solution for finding the kth to last element in a linked list
class Solution:
  def kth_to_last(self, head, k):
    # Traverse k nodes into the linked list
    prev_node = head
    counter = 0
    while prev_node.next and counter < k:
      prev_node = prev_node.next
      counter += 1

    # Move the offset from the beginning of the linked list until the end is reached
    offset = head
    while prev_node.next:
      prev_node = prev_node.next
      offset = offset.next

    return offset.data
