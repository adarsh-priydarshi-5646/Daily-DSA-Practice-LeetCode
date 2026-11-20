# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the result variable inside the function to keep track of the maximum sum
        max_sum = float('-inf')

        # Recursive DFS function to calculate the maximum path sum
        def solve(node):
            nonlocal max_sum  # We will use nonlocal to modify max_sum from the outer function
            if not node:
                return 0

            # Calculate the maximum path sum for the left and right subtrees
            left = max(0, solve(node.left))  # Ignore negative paths
            right = max(0, solve(node.right))  # Ignore negative paths

            # Calculate the current path sum that includes the current node
            curr_path = node.val + left + right

            # Update the global max_sum if the current path sum is greater
            max_sum = max(max_sum, curr_path)

            # Return the maximum path sum from either left or right subtree to the parent node
            return node.val + max(left, right)

        solve(root)
        return max_sum

        