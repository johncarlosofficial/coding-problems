from trees_and_graphs.binary_tree import BinaryTree

tree = BinaryTree()

tree.insert(5)
tree.insert(6)
tree.insert(3)
tree.insert(2)
tree.insert(7)

print(tree.depth_first_search(tree.root, 7))
