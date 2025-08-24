"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        def flattenDFS(prev, curr):
            if curr is None:
                return prev

            curr.prev = prev
            prev.next = curr
            tempNext = curr.next   # store next
            tail = flattenDFS(curr, curr.child)  # recursively flatten child list
            curr.child = None  # child pointer remove kar diya
            return flattenDFS(tail, tempNext)  # continue from saved next

        dummy = Node(0)
        flattenDFS(dummy, head)
        dummy.next.prev = None
        return dummy.next


        