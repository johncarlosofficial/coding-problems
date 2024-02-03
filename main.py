from linked_lists.remove_dups import LinkedList
from linked_lists.remove_dups import Solution

# Create a linked list
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(4)
linked_list.append(3)

# Display the original linked list
print("Original Linked List:")
linked_list.display(linked_list.head)

# Remove duplicates
solution = Solution()
solution.remove_dups(linked_list.head)

# Display the modified linked list
print("\nLinked List after removing duplicates:")
linked_list.display(linked_list.head)