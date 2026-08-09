class Solution:
    def romanToInt(self, s: str) -> int:
        #-- prepare
        romans = [c for c in 'IVXLCDM']       # - IVX LCD M
        ints =  [1, 5, 10, 50, 100, 500, 1000]
        roman_to_int = dict(zip(romans, ints))

        #-- process
        total = 0
        for i in range(len(s)):
            # -- current char less then next ; minus(-) else plus(+) to total ; ex: IV = -1 + 5 = 4
            if i!=len(s)-1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:  
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]                                
        return total
    
sol = Solution()
assert (result:=sol.romanToInt("IV")) ==  4, f'Failed, received:{result}'
assert (result:=sol.romanToInt("III")) ==  3, f'Failed, received:{result}'
assert (result:=sol.romanToInt("LVIII")) ==  58, f'Failed, received:{result}'
assert (result:=sol.romanToInt("MCMXCIV")) ==  1994, f'Failed, received:{result}'
assert (result:=sol.romanToInt("MDCCXLIX")) ==  1749, f'Failed, received:{result}'
