class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        if len(s) != len(t):
            return False
        for i, v in enumerate(s):
            if v not in dic and t[i] not in dic.values():
                dic[v] = t[i]
            else:
                if v not in dic.keys() or dic[v] != t[i]:
                    return False
        print(dic)
        return True


s = "paper"
t = "title"
sol = Solution()
res = sol.isIsomorphic(s, t)
print(res)