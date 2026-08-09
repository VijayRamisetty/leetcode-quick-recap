# Buy & Sell - multiple 
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0 
        for i in range(1, len(prices)):      #----- Remember: Range Starts at 1  
            if prices[i] > prices[i-1]:
                total_profit += (prices[i]  - prices[i-1])
        return total_profit

sol = Solution()
#assert (received:=sol.maxProfit([7,1,5,3,6,4])) == 7, f'Failed {received=}'
assert (received:=sol.maxProfit([1,2,3,4,5])) == 4, f'Failed {received=}'
