# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth=0
        if not root: return maxWidth
        q=deque()
        q.append([root,0])
        while q:
            n=len(q)
            levMin=q[0][1]
            for i in range(n):
                curr_ind=q[0][1]-levMin
                if i==0:
                    first=curr_ind
                if i==n-1:
                    last=curr_ind
                node=q[0][0]
                q.popleft()
                if node.left:
                    q.append([node.left,2*curr_ind+1])
                if node.right:
                    q.append([node.right,2*curr_ind+2])
            maxWidth=max(maxWidth,last-first+1)
        return maxWidth