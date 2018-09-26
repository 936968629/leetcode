class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(s.split())
        print(s)
        if len(s) == 0:
            return True
        i, j = 0, len(s)-1
        while i < j:
            if not s[i].isalpha() and not s[i].isdigit():
                i += 1
                continue
            if not s[j].isalpha() and not s[j].isdigit():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

# str = 'A man, a plan, a canal: Panama'
str = 'race a car'
sol = Solution()
result = sol.isPalindrome(str)
print(result)
