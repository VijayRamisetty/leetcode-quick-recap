class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman_list =[          # -- ORDERED LIST ( BIG to SMALL)
            ( 1000, 'M'),
                            ( 900, 'CM'), #-- special
            (  500, 'D' ),
                            ( 400, 'CD'), #-- special
            (  100, 'C'),
                            ( 90, 'XC'),  #-- special
            (   50, 'L' ),
                            ( 40, 'XL'),  #-- special
            (   10, 'X' ),
                            ( 9, 'IX'),  #-- special
            (    5, 'V' ),
                            ( 4, 'IV'),  #-- special
            (    1, 'I' )
        ]

        res = []
        for val, code in int_to_roman_list:
            if num == 0:
                break
            factor, num = divmod(num, val )      # remeber ; [ factor , num = divmod(num, val) ]
            res.append(factor * code)
        
        return ''.join(res)



sol = Solution()
assert (received:=sol.intToRoman(3749)) == 'MMMDCCXLIX', f'Failed {received=}'
assert (received:=sol.intToRoman(58)) == 'LVIII', f'Failed {received=}'
assert (received:=sol.intToRoman(1994)) == 'MCMXCIV', f'Failed {received=}'