# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre = None
        curr = head
        while curr:
            forword = curr.next
            curr.next = pre
            pre = curr
            curr = forword
        return pre
        