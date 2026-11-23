# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        d = True # L to R = True and R to L = False
        queue = deque([root])

        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                top = queue.popleft()
                level.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            if d:
                result.append(list(level))
            else:
                result.append(list(reversed(level)))
            d = not d
        return result
            