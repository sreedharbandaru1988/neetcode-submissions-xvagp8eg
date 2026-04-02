# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        res =[]
        if root:
            queue.append(root)
        while len(queue) > 0:
            rightmost = None
            for i in range(len(queue)):
                curr = queue.popleft()               
                if curr:
                    rightmost = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            if rightmost:
                res.append(rightmost.val)
        return res
