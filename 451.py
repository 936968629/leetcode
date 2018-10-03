from collections import Counter
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        newstr = ''
        s = Counter(s)
        # s = sorted(s.items(), key=lambda x:x[1], reverse=True)
        print(s)
        for k, v in s.most_common():
            # print(k . v)
            for i in range(v):
                newstr += k
        print(newstr)
        return newstr


parstr = "tree"
sol = Solution()
sol.frequencySort(parstr)