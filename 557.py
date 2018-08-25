class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split()
        # for index in range(len(sList)):
        #     sList[index] = sList[index][::-1]
        # s = ' '.join(sList)
        # print(s)
        resuly = []
        for item in sList:
            resuly.append(item[::-1])
        s = ' '.join(resuly)
        print(s)
        return s

s = "Let's take LeetCode contes"
sol = Solution()
sol.reverseWords(s)