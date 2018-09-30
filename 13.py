class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return False
        rules = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in range(0, len(s)-1):
            if rules[s[i]] < rules[s[i+1]]:
                sum -= rules[s[i]]
            else:
                sum += rules[s[i]]
        sum += rules[s[-1]]
        print(sum)
        return sum


pastr = 'MCMXCIV'
# pastr = 'VIII'
sol = Solution()
sol.romanToInt(pastr)