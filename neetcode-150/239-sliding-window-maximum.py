# The hint is MONOTONIC DECREASING DEQUE

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])

        for r in range(k,len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            if r-k == q[0]:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans



# We dont need the extra For Loop
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for r in range(len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            if r-k == q[0]:
                q.popleft() 
            if r >= k-1:
                ans.append(nums[q[0]])
        
        return ans