from linked_lists.sum_lists import LinkedList, Solution

# Step 1: Instantiate LinkedList objects and append elements
linked_list1 = LinkedList()
linked_list1.append([7, 1, 6])

linked_list2 = LinkedList()
linked_list2.append([5, 9, 2])

# Step 2: Reverse the linked lists
head1 = linked_list1.reverse_list(linked_list1.head)
head2 = linked_list2.reverse_list(linked_list2.head)

# Step 3: Instantiate Solution object and add lists
solution = Solution()
result_head = solution.add_lists(head1, head2)

# Step 4: Reverse the result and display
result_linked_list = LinkedList()
result_linked_list.head = result_head
reversed_result_head = result_linked_list.reverse_list(result_linked_list.head)
result_linked_list.head = reversed_result_head
result_linked_list.display()
