# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return 
        q=deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            l=q.popleft()
            r=q.popleft()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val==r.val:
                q.append(l.left)
                q.append(r.right)
                q.append(l.right)
                q.append(r.left)
            else:
                return False
        return True