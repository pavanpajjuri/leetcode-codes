import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, counter, l))
                counter += 1
        
        dummy = ListNode(-1)
        tail = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next)) 
                counter += 1
            tail = tail.next
        return dummy.next

# TC : O(NlogK)
# SC : O(k)