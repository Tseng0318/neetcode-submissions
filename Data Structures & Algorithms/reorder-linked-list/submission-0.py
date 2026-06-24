# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse second half
        second = slow.next           # head of second half
        slow.next = None       # cut the link
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev
        
        # Step 3: merge 1 → 2 → 3 and 5 → 4:
        first = head
        while second:
            tmp1 = first.next #2
            tmp2 = second.next #4
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        