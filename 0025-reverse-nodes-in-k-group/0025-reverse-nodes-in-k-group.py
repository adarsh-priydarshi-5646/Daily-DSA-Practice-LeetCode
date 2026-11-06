# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1

        if k > length:
            return head
        
        pre = None
        curr = head
        forword = curr.next
        count = 0
        while count < k:
            forword = curr.next
            curr.next = pre
            pre = curr
            curr = forword
            count += 1

        if forword != None:
            ans  = self.reverseKGroup(forword,k)
            head.next = ans
        return pre
        