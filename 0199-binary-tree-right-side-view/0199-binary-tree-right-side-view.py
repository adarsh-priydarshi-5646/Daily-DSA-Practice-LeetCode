# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = deque([root])
        result = []

        while q:
            l_l = len(q)
            for i in range(l_l):
                top = q.popleft()
                if i == l_l - 1:
                    result.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
        return result

        
        