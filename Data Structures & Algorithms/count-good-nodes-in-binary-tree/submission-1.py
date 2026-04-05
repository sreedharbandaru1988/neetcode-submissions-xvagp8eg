# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def preorder(root, maxVal):
            if not root:
                return 0
            if root.val >= maxVal:
                maxVal = root.val
                self.res += 1
            preorder(root.left, maxVal)
            preorder(root.right, maxVal)
        preorder(root, root.val)
        return self.res

        