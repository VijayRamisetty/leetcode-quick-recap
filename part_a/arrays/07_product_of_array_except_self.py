from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix                                 # capture i th result first
            prefix *= nums[i]                               # then calculate the prefix product

        suffix = 1
        for i in range(len(nums)-1, -1, -1):                # --- reverse range 
            res[i] *=suffix
            suffix *= nums[i]
        
        return res

sol = Solution()
assert (result:=sol.productExceptSelf([1,2,3,4])) == [24,12,8,6], f'Failed, received:{result}'
assert (result:=sol.productExceptSelf([-1,1,0,-3,3])) == [0,0,9,0,0], f'Failed, received:{result}'
