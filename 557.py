class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split()
        print(sList)
        for index in range(len(sList)):
            sList[index] = sList[index][::-1]
        s = ' '.join(sList)
        print(s)
        return s

s = "Let's take LeetCode contes"
sol = Solution()
sol.reverseWords(s)