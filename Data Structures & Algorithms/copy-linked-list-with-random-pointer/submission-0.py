"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {None: None}     # ← pre-populated trick for None lookups
        
        # Pass 1: create copies (values only)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)          # add curr → new Node(curr.val) to map
            curr = curr.next
        
        # Pass 2: wire up next and random
        curr = head
        while curr:
            copy = old_to_new[curr]                # look up curr's copy
            copy.next = old_to_new[curr.next]         # look up curr.next's copy
            copy.random = old_to_new[curr.random]         # look up curr.random's copy
            curr = curr.next
        
        return old_to_new[head]                    # the head of the copy     