# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.balanced = True
    def height(self,root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        if self.balanced == True and abs(lh - rh) > 1:
            self.balanced = False
        return max(lh,rh) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.balanced
        