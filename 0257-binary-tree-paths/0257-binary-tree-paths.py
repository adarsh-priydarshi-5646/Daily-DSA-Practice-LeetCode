# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node, path):
            if not node:
                return

            # Current path add karo
            path += str(node.val)

            # Agar leaf node hai -> result me store kar do
            if not node.left and not node.right:
                result.append(path)
                return

            # Agar leaf nahi hai -> "->" lagake children me jao
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return result

