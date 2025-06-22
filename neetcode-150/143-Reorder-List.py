# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        p1 = head
        p2 = prev

        while p1 and p2:
            temp1 = p1.next
            p1.next = p2
            p1 = temp1

            temp2 = p2.next
            p2.next = p1
            p2 = temp2

        if p1:
            p1.next = None
        
    # TC: O(n)
    # SC: O(1)
    