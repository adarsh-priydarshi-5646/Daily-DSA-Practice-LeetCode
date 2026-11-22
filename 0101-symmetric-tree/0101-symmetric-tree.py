# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque()
        q.append((root.left, root.right))

        while q:
            left, right = q.popleft()

            # Dono null → continue
            if not left and not right:
                continue

            # Agar koi ek null → not symmetric
            if not left or not right:
                return False

            # Values match nahi → not symmetric
            if left.val != right.val:
                return False

            # Push outer pair: left.left - right.right
            q.append((left.left, right.right))
            # Push inner pair: left.right - right.left
            q.append((left.right, right.left))

        return True
        
        