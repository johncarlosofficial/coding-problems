from typing import List, Optional

class TreeNode:
    def __init__(self, value: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, nums: List[int]) -> str:
        if not nums:
            return "No values were inserted into the tree."

        for num in nums:
            self._insert_node(num)
        
        return "Your value(s) were inserted into the tree."

    def _insert_node(self, value: int):
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
            return

        curr_node = self.root
        while curr_node:
            if new_node.value > curr_node.value:
                if not curr_node.right:
                    curr_node.right = new_node
                    return
                curr_node = curr_node.right
            else:
                if not curr_node.left:
                    curr_node.left = new_node
                    return
                curr_node = curr_node.left

    def search(self, value: int) -> Optional[tuple]:
        parent_node = None
        curr_node = self.root
        
        while curr_node:
            if value == curr_node.value:
                return parent_node, curr_node
            parent_node = curr_node
            if value < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return "This value doesn't exist in the tree."

    def in_order_traversal(self) -> List[int]:
        result = []
        self._in_order_helper(self.root, result)
        return result

    def _in_order_helper(self, node: Optional[TreeNode], result: List[int]):
        if node:
            self._in_order_helper(node.left, result)
            result.append(node.value)
            self._in_order_helper(node.right, result)

    def delete(self, value: int) -> str:
        if not value:
            return "You didn't inform a value to be deleted."
        if not self.root:
            return "The tree is already empty."
        
        search_result = self.search(value)
        if isinstance(search_result, str):
            return search_result
        parent_node, curr_node = search_result

        # Node with no children (leaf node)
        if not curr_node.left and not curr_node.right:
            self._delete_leaf_node(parent_node, curr_node)
        
        # Node with one child
        elif not curr_node.left or not curr_node.right:
            self._delete_single_child_node(parent_node, curr_node)
        
        # Node with two children
        else:
            self._delete_two_children_node(curr_node)
        
        return f"Node with value {value} deleted from the tree."

    def _delete_leaf_node(self, parent_node: Optional[TreeNode], curr_node: TreeNode):
        if not parent_node:  # Deleting root
            self.root = None
        elif parent_node.left == curr_node:
            parent_node.left = None
        else:
            parent_node.right = None

    def _delete_single_child_node(self, parent_node: Optional[TreeNode], curr_node: TreeNode):
        child_node = curr_node.left if curr_node.left else curr_node.right
        if not parent_node:  # Deleting root node
            self.root = child_node
        elif parent_node.left == curr_node:
            parent_node.left = child_node
        else:
            parent_node.right = child_node

    def _delete_two_children_node(self, curr_node: TreeNode):
        # Find in-order successor (smallest in right subtree)
        successor_parent, successor = self._find_in_order_successor(curr_node)
        
        # Replace current node's value with successor's value
        curr_node.value = successor.value
        
        # Delete the successor node
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

    def _find_in_order_successor(self, node: TreeNode) -> tuple:
        parent = node
        successor = node.right
        while successor.left:
            parent = successor
            successor = successor.left
        return parent, successor

    def print_tree(self):
      if not self.root:
        print("The tree is empty.")
        return

      # BFS (level-order traversal) using a queue
      queue = deque([self.root])
      while queue:
        level_size = len(queue)
        level_nodes = []

        node = queue.popleft()

        if node:
          level_nodes.append(str(node.value))
          queue.append(node.left)
          queue.append(node.right)

        else:
          level_nodes.append("None")

      print(" | ".join(level_nodes))
      
# Example Usage
tree = Tree()
print(tree.insert([5, 3, 7, 2, 4, 6, 8]))
print(tree.delete(5))
print(tree.search(5))
print(tree.in_order_traversal())
tree.print_tree()
