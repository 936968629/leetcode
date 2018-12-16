class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = ['a','e','i','o','u']
        i = 0
        j = len(s) - 1
        strList = list(s)
        while i < j:
            if strList[i].lower() not in yuan:
                i += 1
            elif strList[j].lower() not in yuan:
                j -= 1
            else:
                strList[i], strList[j] = strList[j], strList[i]
                i += 1
                j -= 1
        s = ''.join(strList)
        # print(s)
        return s

s = "jianzhioffer"
sol = Solution()
sol.reverseVowels(s)


# leotcede

'''
注意大小写
'''