# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # Find the k-th node from group_prev
            kth = self.get_kth(group_prev, k)
            if not kth:
                break                     # fewer than k nodes remain
            
            group_next = kth.next          # what comes after the group
            
            # Reverse the group: from group_prev.next to kth
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Stitch back
            new_tail = group_prev.next    # was the first node of the group, now the last
            group_prev.next = kth          # was the last, now the head of the reversed group
            group_prev = new_tail          # advance to the new tail for next iteration
        
        return dummy.next
    
    def get_kth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node        