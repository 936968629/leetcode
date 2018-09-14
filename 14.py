class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        n = len(strs)
        if n == 0:
            return ""
        res = ""
        strs.sort()  # sort the string array
        first = strs[0]
        last = strs[-1]
        limit = min(len(first), len(last))
        for i in range(limit):  # find out the longest common prefix between first and last word
            if first[i] == last[i]:
                res += first[i]
            else:
                break
        return res

        '''
        liststr = zip(*strs)
        result = ''
        for i in zip(*strs):
            a = i[0]
            for j in i[1:]:
                if a != j:
                    return result
            else:
                result += a
        return result
        '''

strs = ["flower", "flow", "flight"]
sol = Solution()
result = sol.longestCommonPrefix(strs)
print(result)
