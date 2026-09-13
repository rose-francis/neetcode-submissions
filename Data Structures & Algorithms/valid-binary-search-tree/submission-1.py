# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        il=[]

        def inorder(root):
            if not root:
                return None
            
            inorder(root.left)
            il.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(1,len(il)):
            if il[i-1]>=il[i]:
                return False
        
        return True