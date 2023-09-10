# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return 
        def level(node,x,lev):
            if not node:
                return 0
            if node==x:
                return lev
            l=level(node.left,x,lev+1)
            if l:
                return l
            return level(node.right,x,lev+1)

        def isSiblings(node,x,y):
            if not node: return False
            return ((node.left==x and node.right==y) or (node.left==y and node.right==x) or isSiblings(node.left,x,y) or isSiblings(node.right,x,y))

        def findNode(node,x):
            if not node: return
            if node.val==x:
                return node
            n=findNode(node.left,x)
            if n:
                return n
            return findNode(node.right,x)

        xx=findNode(root,x)
        yy=findNode(root,y)
        return ((level(root,xx,0)==level(root,yy,0))) and (not isSiblings(root,xx,yy))