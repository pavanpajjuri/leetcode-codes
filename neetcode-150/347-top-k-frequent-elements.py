# O(nlogn) Worst Case
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = sorted(c.items(), key = lambda x : x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(c[i][0])
        return ans
    
    
# O(nlogk) solution
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for key,v in c.items():
            heapq.heappush(heap, (v,key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [v for (key,v) in heap]
