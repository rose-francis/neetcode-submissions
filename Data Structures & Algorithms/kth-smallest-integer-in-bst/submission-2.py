# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i=0
        def inorder(node):
            if node is None:
                return None
            left= inorder(node.left)
            if left is not None:
                return left
            self.i+=1
            if self.i==k:
                return node.val
            
            return inorder(node.right)

        return inorder(root)
