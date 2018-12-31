class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.res = []
        self.helper(digits, dic, '', 0)
        return self.res

    def helper(self, digits, dic, item, i):

        if len(digits) == len(item):
            self.res.append(item[:])
            return
        word = digits[i]
        for j in range(len(dic[word])):
            self.helper(digits, dic, item + dic[word][j], i+1)

digits = '23'
sol = Solution()
res = sol.letterCombinations(digits)
print(res)