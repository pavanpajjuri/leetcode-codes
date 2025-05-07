from collections import defaultdict
class Solution:
    def is_subset(self, count_t, count_s):
        for k,v in count_t.items():
            if count_s.get(k, 0) < v:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)

        if n1 < n2:
            return ""

        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for i in range(n2):
            count_t[t[i]] += 1
            count_s[s[i]] += 1
        
        if count_s == count_t:
            return s[:n2]
        
        l = 0
        ans = [0,0]
        min_len = float('inf')
        for r in range(n2,n1):
            count_s[s[r]] += 1
            while self.is_subset(count_t, count_s):
                if r-l+1 < min_len:
                    min_len = min(min_len, r-l+1)
                    ans = [l,r+1]
                count_s[s[l]] -= 1
                l += 1
        
        return s[ans[0]:ans[1]]



# More Faster Solution
from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)

        if n1 < n2:
            return ""

        count_s = defaultdict(int)
        count_t = Counter(t)

        l = 0
        ans = [0,0]
        have = 0
        need = len(count_t)
        min_len = float('inf')
        for r in range(n1):
            char = s[r]
            count_s[char] += 1

            if char in count_t and count_s[char] == count_t[char]:
                have += 1

            while have == need:
                if r-l+1 < min_len:
                    min_len = min(min_len, r-l+1)
                    ans = [l,r+1]
                    
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        
        return s[ans[0]:ans[1]]
