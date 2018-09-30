from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = dict(Counter(s))
        t = dict(Counter(t))
        print(s == t)
        return s == t


s1 = 'anagram'
s2 = 'nagaram'
sol = Solution()
sol.isAnagram(s1, s2)