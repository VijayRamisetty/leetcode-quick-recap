class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            sum_of_squares=sum( [int(x)**2 for x in str(n)])
            n = sum_of_squares
            if n in seen:
                return False
            seen.add(n)
        return True


sol = Solution()
assert((received:=sol.isHappy(n=19))) == True, f'Failed {received=}'
assert((received:=sol.isHappy(n=2))) == False, f'Failed {received=}'

