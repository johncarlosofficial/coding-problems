# Binary tree playground; depth-first search


class TreeNode:

  def __init__(self, num=0):
    self.val = num
    self.left = None
    self.right = None


class BinaryTree:

  def __init__(self):
    self.root = None

  def insert(self, num):
    if not self.root:
      self.root = TreeNode(num)
    else:
      self.insert_recursive(self.root, num)

  def insert_recursive(self, node, num):
    if num < node.val:
      if not node.left:
        node.left = TreeNode(num)
      else:
        self.insert_recursive(node.left, num)

    elif num > node.val:
      if not node.right:
        node.right = TreeNode(num)
      else:
        self.insert_recursive(node.right, num)

  def depth_first_search(self, node, num):
    if not node:
      return None

    if num == node.val:
      return num

    if num > node.val:
      return self.depth_first_search(node.right, num)

    else:
      return self.depth_first_search(node.left, num)
