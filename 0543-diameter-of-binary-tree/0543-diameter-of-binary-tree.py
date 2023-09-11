# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def longest_path(root):
            if not root: return 0
            nonlocal diameter
            left_height=longest_path(root.left)
            right_height=longest_path(root.right)
            diameter=max(diameter,left_height+right_height)
            return max(left_height,right_height)+1
        longest_path(root)
        return diameter