# Array Solution
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==1 or n==2:
            return 0
        
        left = [0]*n
        right = [0]*n 
        curr_left_max = curr_right_max = float('-inf')

        for i in range(n):
            left[i] = curr_left_max = max(curr_left_max, height[i])
            right[n-1-i] = curr_right_max = max(curr_right_max, height[n-1-i])
        
        ans = 0
        for i in range(1,n):
            ans += max(0, min(left[i], right[i])-height[i])
        
        return ans
    

# Two Pointer Solution Derived From array Solution. More Faster    
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        curr_left_max = curr_right_max = 0
        ans = 0
        while l < r:
            curr_left = height[l]
            curr_right = height[r]
            if curr_left <= curr_right:
                curr_left_max = max(curr_left_max, curr_left)
                ans += curr_left_max - curr_left
                l += 1
            else:
                curr_right_max = max(curr_right_max, curr_right)
                ans += curr_right_max - curr_right
                r -= 1
        
        return ans





