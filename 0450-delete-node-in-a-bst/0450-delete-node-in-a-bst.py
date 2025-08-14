# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Traverse left or right
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted found
            # Case 1: No child
            if root.left is None and root.right is None:
                return None
            # Case 2: One child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 3: Two children
            min_node = self.get_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root

    def get_min(self, node):
        while node.left:
            node = node.left
        return node
