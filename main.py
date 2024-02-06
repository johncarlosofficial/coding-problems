from linked_lists.partition import LinkedList, Solution

linkedlist = LinkedList()
linkedlist.append([5,3,7,8,2])

solution = Solution()
new_head = solution.partition(linkedlist.head, 3)

linkedlist.display(new_head)