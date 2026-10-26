# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #  Next node ka value uthaya aur current node me daal diya
        node.val = node.next.val
        # ↑ Ab current node ka data change ho gaya hai (5 → 1 ban gaya)

        #  Current node ka next pointer ko update kiya
        node.next = node.next.next
        # ↑ Ab next node list se hat gaya (uska pointer hata diya)