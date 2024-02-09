from linked_lists.palindrome import LinkedList, Solution

linked_list = LinkedList()
linked_list.append([1, 2, 3, 2, 1])

solution = Solution()
print(solution.palindrome(linked_list.head))