# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(leftmax,0)
            rightmax = max(rightmax,0)
            self.res = max(self.res, leftmax + rightmax+ root.val)
            maxValue = root.val + max(leftmax, rightmax)
            return maxValue
        dfs(root)
        return self.res
        