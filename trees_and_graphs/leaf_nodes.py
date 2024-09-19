from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def insert(self, nums: List[int]):
        for num in nums:
            if not self.root:
                self.root = TreeNode(num)
            else:
                curr_node = self.root
                while True:
                    if num > curr_node.val:
                        if not curr_node.right:
                            curr_node.right = TreeNode(num)
                            break
                        curr_node = curr_node.right
                            
                    else:
                        if not curr_node.left:
                            curr_node.left = TreeNode(num)
                            break
                        curr_node = curr_node.left

class Solution:
    def findLeafNodes(self, root):
        if not root:
            return
        
        ans = []
        
        def traverse(node):
            nonlocal ans
            
            if not node:
                return
            
            if not node.left and not node.right:
                ans.append(node.val)
            
            traverse(node.left) 
            traverse(node.right)
        
        traverse(root)
        return ans
            
tree = Tree()
tree.insert([100, 80, 120, 70, 85, 110, 130])

solution = Solution()
print(solution.findLeafNodes(tree.root))
            