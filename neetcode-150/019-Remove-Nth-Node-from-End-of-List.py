# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        curr = head
        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        while curr:
            if k >= n:
                slow = slow.next
            curr = curr.next
            k += 1
        if slow:
            slow.next = slow.next.next
        return dummy.next


        # TC : O(n)
        # SC : O(1)
