from linked_lists.return_kth_to_last import LinkedList, Solution


instance = LinkedList()
instance.append([1, 2, 3, 4, 5, 6])
print(instance.display(instance.head))

sol = Solution()
print(sol.kth_to_last(instance.head, 1))