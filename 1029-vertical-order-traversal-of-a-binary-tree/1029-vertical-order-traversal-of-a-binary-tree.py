# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(list)
        q=deque()
        q.append([root,0,0])
        while q:
            node,vertical,level=q.popleft()
            d[vertical].append([node.val,level])
            if node.left:
                q.append([node.left,vertical-1,level+1])
            if node.right:
                q.append([node.right,vertical+1,level+1])
        ans=[]
        for i in sorted(d.keys()):
            lst=d[i]
            lst.sort(key=lambda x:(x[1],x[0]))
            temp=[]
            for i in lst:
                temp.append(i[0])
            ans.append(temp)
        return ans