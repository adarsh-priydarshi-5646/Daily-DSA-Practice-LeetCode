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
        
        def flattenDFS(previousNode, currentNode):
            if currentNode is None:
                return previousNode

            currentNode.prev = previousNode
            previousNode.next = currentNode

            tempNext = currentNode.next   # store next
            tail = flattenDFS(currentNode, currentNode.child)  # recursively flatten child list
            currentNode.child = None  # child pointer remove kar diya

            return flattenDFS(tail, tempNext)  # continue from saved next

        dummy = Node(0, None, None, None)
        flattenDFS(dummy, head)
        dummy.next.prev = None
        return dummy.next


        