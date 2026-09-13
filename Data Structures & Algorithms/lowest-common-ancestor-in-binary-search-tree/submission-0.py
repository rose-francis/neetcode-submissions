# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res=None
        def dfs(root):
            if (p.val>root.val and q.val<root.val) or (p.val<root.val and q.val>root.val):
                self.res=root
            elif (p.val>root.val and q.val>root.val):
                dfs(root.right)
            elif (p.val<root.val and q.val<root.val):
                dfs(root.left)
            elif (p.val==root.val):
                self.res=p
            elif (q.val==root.val):
                self.res=q
        
        dfs(root)
        return self.res
        