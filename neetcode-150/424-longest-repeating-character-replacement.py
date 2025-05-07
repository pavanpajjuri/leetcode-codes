class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = max_freq = l = 0
        count = [0]*26

        for r in range(len(s)):
            count[ord(s[r])-ord('A')] += 1
            max_freq = max(count)
            while (r-l+1) - max_freq > k:
                count[ord(s[l])-ord('A')] -= 1
                l += 1
            ans = max(ans, r-l+1)
        
        return ans
    
    
# You can overestimate max_freq, but you must not underestimate it — so it’s safe to update only during expansion. That means max_freq need not be updated

from collections import defaultdict
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        d = defaultdict(int)
        ans = 0
        max_freq = 0
        for r in range(n):
            d[s[r]] += 1
            max_freq = max(max_freq,d[s[r]])
            
            while (r-l+1)-max_freq > k:
                d[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)

        return ans
