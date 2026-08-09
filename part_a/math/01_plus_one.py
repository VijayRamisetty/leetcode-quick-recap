from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # -- EDGE                               #-- Example : [9] -> [1] & append 0 
        if len(digits) == 0:
            return [1]

        if digits[-1]!=9:
            digits[-1] +=1
        else:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
        return digits

sol = Solution()
assert (received:=sol.plusOne([1,2,3])) == [1,2,4], f'Failed:  {received=}'
assert (received:=sol.plusOne([4,3,2,1])) == [4,3,2,2], f'Failed:  {received=}'
assert (received:=sol.plusOne([9])) == [1,0], f'Failed:  {received=}'
assert (received:=sol.plusOne([1,9,8,9])) == [1,9,9,0], f'Failed:  {received=}'
assert (received:=sol.plusOne([9,9,9,9])) == [1,0,0,0,0], f'Failed:  {received=}'
