# Implement a function to check if a linked list is a palindrome.

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
        
  def display(self):
    curr_node = self.head

    while curr_node:
      print(curr_node.val, end=" -> ")
      curr_node = curr_node.next
      
    print("None")

class Solution:
  def palindrome(self, head_node):
    # Create an empty list to store values from the linked list
    original_list = []
    curr_node = head_node
    while curr_node:
      original_list.append(curr_node.val)
      curr_node = curr_node.next

    # Initialize two pointers for checking palindrome
    left = 0
    right = len(original_list) - 1

    while left < right:
      if original_list[left] != original_list[right]:
        return False
      left += 1
      right -= 1

    return True

      
