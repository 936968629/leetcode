class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        length = len(s)
        if length == 0:
            return ''
        i = 0
        j = length - 1
        str_list = list(s)
        while i < j:
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1
        s = ''.join(str_list)
        # print(s)
        return s

s = "hello world"
sol = Solution()
sol.reverseString(s)
