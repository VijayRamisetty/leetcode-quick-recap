class Solution:
    def isPalindrome(self, x: int) -> bool:
        # -- Edge
        if x < 0 : return False
        if x == 0 : return True
        if x % 10 == 0 : return False

        # -- Regular
        oldX = x
        newX = 0
        while x!=0:                             #-- REMEBER : while x!=0
            x, last_digit = divmod(x ,10) 
            newX = newX * 10 + last_digit
        
        return oldX == newX

sol = Solution()
assert (received:=sol.isPalindrome(x=121)) == True, f'Failed: {received=}'
assert (received:=sol.isPalindrome(x=-121)) == False, f'Failed: {received=}'
assert (received:=sol.isPalindrome(x=10)) == False, f'Failed: {received=}'
assert (received:=sol.isPalindrome(x=172161271)) == True, f'Failed: {received=}'