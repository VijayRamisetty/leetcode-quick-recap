from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = []
        for i, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1][0]]:  # current > top_of_stack
                popped_index, val = stack.pop()
                res[popped_index] = i - popped_index
            stack.append((i, current_temp))
        
        return res

sol = Solution()
assert (received:=sol.dailyTemperatures([73,74,75,71,69,72,76,73])) == [1,1,4,2,1,1,0,0], f'Failed {received=}'
assert (received:=sol.dailyTemperatures([30,40,50,60])) == [1,1,1,0], f'Failed {received=}'
assert (received:=sol.dailyTemperatures([30,60,90])) == [1,1,0], f'Failed {received=}'
