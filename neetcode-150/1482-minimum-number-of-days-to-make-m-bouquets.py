class Solution:
    def is_feasible(self, bloomDay, mid, m, k):
        bq = fl = 0
        for x in bloomDay:
            if x <= mid:
                fl += 1
                if fl == k:
                    bq += 1
                    fl = 0
            else:
                fl = 0
        return bq >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        l,r = 1, max(bloomDay)
        while l < r:
            mid = (l+r)//2
            if self.is_feasible(bloomDay, mid, m, k):
                r = mid
            else:
                l = mid + 1
        
        return l