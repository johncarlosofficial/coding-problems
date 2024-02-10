# Given two (singly) linked lists, determine if the two lists intersect. 
# Return the intersecting node. Note that the intersection if defined 
# based on reference, not value. That is, if the kth node of the first 
# linked list is the exact same node (by reference) as the jth node of 
# the second linked list, then they are intersecting.

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

class Solution:
  def get_size_and_tail(self, head):
    curr_node = head
    size = 1

    while curr_node.next:
      curr_node = curr_node.next
      size += 1

    return size, curr_node
    
  def intersection(self, head1, head2):
    size1, tail1 = self.get_size_and_tail(head1)
    size2, tail2 = self.get_size_and_tail(head2)

    # If the tails are different, there's no intersection
    if tail1 != tail2:
      return False

    # Set two pointers to the start of each linked list
    curr1 = head1
    curr2 = head2

    # Advance the pointer on the longer linked list by the difference in lengths
    if size1 > size2:
      for _ in range(size1 - size2):
        curr1 = curr1.next
    
    elif size2 > size1:
      for _ in range(size2 - size1):
        curr2 = curr2.next

    # Traverse on each linked list until the pointers are the same
    while curr1 != curr2:
      curr1 = curr1.next
      curr2 = curr2.next

    return curr1 # Return the intersecting node
      
      
    