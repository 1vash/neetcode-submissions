# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal diameter

            max_left_path = dfs(node.left)
            max_right_path = dfs(node.right)

            diameter = max(diameter, max_left_path + max_right_path)
            
            return 1 + max(max_left_path, max_right_path) 


        dfs(root)
        return diameter