# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        curr_sum = 0
        if root.val >= low and root.val <= high:
            curr_sum += root.val
            curr_sum += self.rangeSumBST(root.left,low,high)
            curr_sum += self.rangeSumBST(root.right,low,high)
        elif root.val < low:
            curr_sum += self.rangeSumBST(root.right,low,high)
        else:
            curr_sum += self.rangeSumBST(root.left,low,high)
        return curr_sum
        