# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds two numbers and returns the sum as a linked list.

# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sum_lists(self, l1, l2):
        # Keep track of the resulting linked list
        dummy_node = ListNode()
        # Pointer to the current node
        curr_node = dummy_node
        # Keep track of the carry
        carry = 0

        while l1 or l2 or carry:
            # Extract the value of the current nodes, defaulting to 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the total value considering the current digits and carry
            total = val1 + val2 + carry

            # Determine the new carry and the resulting digit after addition
            carry = total // 10
            rest = total % 10

            # Append a new node with the resulting digit to the result linked list
            curr_node.next = ListNode(rest)
            # Move the pointer to the next node
            curr_node = curr_node.next

            # Move to the next nodes in the input linked lists if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the resulting linked list
        return dummy_node.next
