class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #-- EDGE Case
        if numRows > len(s) or numRows == 1:
            return s
        #-- Regular 
        res = [''] * numRows
        current_row = 0
        direction = -1

        for c in s:
            #-- add
            res[current_row] += c
            #-- decide direction
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            #-- move up or down
            current_row +=direction
        return ''.join(res)

sol = Solution()
assert (received:=sol.convert('PAYPALISHIRING', 3)) == 'PAHNAPLSIIGYIR', f'Failed {received=}'
assert (received:=sol.convert('PAYPALISHIRING', 4)) == 'PINALSIGYAHRPI', f'Failed {received=}'
assert (received:=sol.convert('PAYPALISHIRING', 1)) == 'PAYPALISHIRING', f'Failed {received=}'
assert (received:=sol.convert('PAYPALISHIRING', 1)) == 'PAYPALISHIRING', f'Failed {received=}'
