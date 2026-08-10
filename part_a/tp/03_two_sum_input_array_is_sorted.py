from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            current_sum = numbers[l] + numbers[r]

            if current_sum > target:
                r-=1
            elif current_sum < target:
                l+=1
            else:
                return [l+1 , r+1]
            
        return []                           #---- Note: Outer return 


sol = Solution()
assert((received:=sol.twoSum(numbers = [2,7,11,15], target = 9))) == [1,2], f'Failed {received=}'
assert((received:=sol.twoSum(numbers = [2,3,4], target = 6))) == [1,3], f'Failed {received=}'
assert((received:=sol.twoSum(numbers = [-1,0], target = -1))) == [1,2], f'Failed {received=}'