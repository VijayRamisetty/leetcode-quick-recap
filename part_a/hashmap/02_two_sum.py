from typing import List
class Solution:
    # retun indices
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            need = target - n 
            if need in seen.keys():             # seen.keys() | seen 
                return [seen[need], i]
            seen[n] = i

sol = Solution()
assert (received:=sol.twoSum(nums = [2,7,11,15], target = 9)) == [0,1], f'Failed {received=}'
assert (received:=sol.twoSum(nums = [3,2,4], target = 6)) == [1,2], f'Failed {received=}'
assert (received:=sol.twoSum(nums = [3,3], target = 6)) == [0,1], f'Failed {received=}'