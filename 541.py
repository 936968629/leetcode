class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        direction = -1
        result = ''
        for i in range(0, len(s), k):
            if i + k < len(s):
                result += s[i:k+i][::direction]
            else:
                result += s[i:k+i]
            direction *= -1
            # reverseStr = s[i:k][::-1]
            # print(i)
        print(result)
        return result


s = "abcdefg"
k = 2
sol = Solution()
sol.reverseStr(s, k)