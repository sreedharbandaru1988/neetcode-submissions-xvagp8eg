# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        def postorder(self, root):
            if not root:
                return None           
            postorder(self, root.left)
            postorder(self, root.right)
            res.append(root.val)
        postorder(self,root)
        return res
        