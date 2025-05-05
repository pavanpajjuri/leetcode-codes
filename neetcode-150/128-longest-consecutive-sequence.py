class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if num+1 in nums_set:
                continue
            count = 1
            while num-count in nums_set:
                count += 1
            ans = max(ans, count)
        return ans


        