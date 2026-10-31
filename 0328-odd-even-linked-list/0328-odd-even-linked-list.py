# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = head              # 1st node (odd group head)
        even = head.next        # 2nd node (even group head)
        even_head = even        # Save even list's starting point

        # Rearranging nodes
        while even and even.next:
            odd.next = even.next  # Link to next odd node
            odd = odd.next        # Move odd pointer

            even.next = odd.next  # Link to next even node
            even = even.next      # Move even pointer

        # Join end of odd list to start of even list
        odd.next = even_head

        return head