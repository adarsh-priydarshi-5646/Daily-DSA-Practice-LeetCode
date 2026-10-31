# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        slow = fast = dummy
        
        # Move fast pointer n + 1 steps ahead so slow lands right before the target
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # Delete the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next

