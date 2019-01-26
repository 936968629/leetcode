class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cache = {}
        if len(s) < 10:
            return []

        i = 0
        j = 9
        while j < len(s):
            if s[i:j+1] in cache:
                cache[ s[i:j+1] ] += 1
            else:
                cache[ s[i:j+1] ] = 0
            i += 1
            j += 1
        res = {i:v for i,v in cache.items() if v > 0}
        print(cache)
        return list(res.keys())

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
sol = Solution()
res =sol.findRepeatedDnaSequences(s)
print(res)