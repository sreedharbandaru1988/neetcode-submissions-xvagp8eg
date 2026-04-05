# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res =[]
        queue = collections.deque()
        if root:
            queue.append(root)
        while len(queue) > 0:
            res1 = []
            for i in range(len(queue)):
                curr = queue.popleft()     
                res1.append(curr.val)         
                if curr.left:                   
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if res1:
                res.append(res1)
        return res

        