# O(n*klogk) soln
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for x in strs:
            c = tuple(sorted(x))
            ans[c].append(x)
        return [v for k,v in ans.items()]

# O(n*k) soln
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for x in strs:
            count = [0]*26
            for s in x:
                count[ord(s)-ord('a')] += 1
            ans[tuple(count)].append(x)
        return [v for k,v in ans.items()]