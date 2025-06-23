# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(start, end):
            prev = None
            curr = start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev, start

        if not head or k == 1:
            return head
        
        dummy = ListNode(-1, head)
        prev_group_tail = dummy
        curr = head
        while curr:
            group_start = curr
            count = 0
            while count < k and curr:
                count += 1
                curr = curr.next
            
            if count < k:
                break

            reversed_head, reversed_tail = reverse(group_start, curr)
            prev_group_tail.next = reversed_head
            reversed_tail.next = curr
            prev_group_tail = reversed_tail
            
            
        
        return dummy.next

        # TC:O(n)
        # SC:O(1)

        

        