# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans=0
        q=deque()
        q.append([root,0])
        while q:
            n=len(q)
            levMin=q[0][1]
            for i in range(n):
                node,num=q[0]
                q.popleft()
                curr_index=num-levMin
                if i==0: leftMost=curr_index
                if i==n-1: rightMost=curr_index
                if node.left:
                    q.append([node.left,curr_index*2+1])
                if node.right:
                    q.append([node.right,curr_index*2+2])
            ans=max(ans,rightMost-leftMost+1)
        return ans