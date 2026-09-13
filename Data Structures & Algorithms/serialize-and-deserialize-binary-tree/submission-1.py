# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        s=[]
        q=collections.deque([root])
        while q:
            node=q.popleft()
            if node:
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                s.append("None")
        return " ".join(s)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="":
            return None
        l=data.split()
        root=TreeNode(int(l[0]))
        q=collections.deque([root])
        i=1
        while q:
            node=q.popleft()
            if node:
                if l[i]!="None":
                    node.left=TreeNode(int(l[i]))
                    q.append(node.left)
                i+=1
                if l[i]!="None":
                    node.right=TreeNode(int(l[i]))
                    q.append(node.right)
                i+=1
        return root




