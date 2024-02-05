from linked_lists.delete_middle_node import LinkedList, Solution

linked_list = LinkedList()
linked_list.append([1, 2, 3, 4, 5, 6])

solution = Solution()
solution.delete_middle_node(linked_list.head.next.next.next)
print(linked_list.display(linked_list.head))
