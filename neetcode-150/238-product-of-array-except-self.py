class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_arr = [1]*n
        r_arr = [1]*n

        for i in range(1,n):
            l_arr[i] = l_arr[i-1]*nums[i-1]
            r_arr[n-1-i] = r_arr[n-i]*nums[n-i]
        return [l_arr[i]*r_arr[i] for i in range(n)]
    
    
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]
        
        R = 1

        for i in range(n-1,-1,-1):
            res[i] = res[i]*R
            R = R*nums[i]
        
        return res