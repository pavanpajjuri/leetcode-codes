class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums_dict = {}
        # for x in nums:
        #     if x in nums_dict:
        #         return True
        #     else:
        #         nums_dict[x] = '1'
        # return False

        return len(nums) != len(set(nums))