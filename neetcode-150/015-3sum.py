class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            target = -nums[i]
            while j < k:
                val = nums[j] + nums[k]
                if val == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif val > target:
                    k -= 1    
                else:
                    j += 1
                    
        
        return ans