# Given a circular linked list, implement an algorithm that
# returns the node at the beginning of the loop.


class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class Solution:
  # Implementation of the "Tortoise and Hare" algorithm
  def loop_detection(self, head_node):
    slow = head_node
    fast = head_node

    # Find meeting point
    while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        break

    # Error check - no meeting point, and therefore no loop
    if fast is None or fast.next is None:
      return None

    # Move slow to head, keep fast at meeting point.
    # Each are k steps from the loop start. If they move at the same pace,
    # they must meet at the loop start.
    fast = head_node
    while slow != fast:
      fast = fast.next
      slow = slow.next

    # Both now point to the start of the loop
    return slow
