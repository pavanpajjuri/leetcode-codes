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
        # if not head:
        #     return None
        # h = defaultdict(Node)
        # curr = head
        # while curr:
        #     h[curr] = Node(curr.val)
        #     curr = curr.next
        
        # curr = head
        # while curr:
        #     node = h[curr]
        #     if curr.next:
        #         node.next = h[curr.next]
        #     if curr.random:
        #         node.random = h[curr.random]
        #     curr = curr.next
        
        # return h[head]

        # TC : O(n)
        # SC : O(n)

        if not head:
            return None
        # Creating copies in between
        curr = head
        while curr:
            copy = Node(curr.val)
            
            copy.next = curr.next
            temp = curr.next
            curr.next = copy
            curr = temp
        
        curr = head
        while curr: 
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        dummy = Node(-1)
        tail = dummy
        curr = head
        while curr:
            tail.next = curr.next
            curr = curr.next.next
            tail = tail.next
        return dummy.next

        # TC : O(n)
        # SC : O(1)