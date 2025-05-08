#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 19:54:07 2025

@author: pavanpaj
"""

# Two Pass Solution
class Solution:
    def atmost(self, nums,k):
        l = ans = count =  0
        for r in range(len(nums)):
            if nums[r]%2 == 1:
                count += 1
            while count > k:
                if  nums[l]%2 == 1:
                    count -= 1
                l += 1  
            ans += r-l+1   
        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k-1)
       
    
# One Pass Solution - Additional Pointer to keep doubling the subarray count when necessary    
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = ans = count = prefix =  0
        for r in range(len(nums)):
            if nums[r]%2 == 1:
                count += 1
                prefix = 0
            while count == k:
                prefix += 1
                if  nums[l]%2 == 1:
                    count -= 1
                l += 1  
            ans += prefix
        return ans