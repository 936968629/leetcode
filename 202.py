class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        notedict = []
        while n != 1:
            n = str(n)
            sum = 0
            for item in n:
                sum += int(item) ** 2
            if sum in notedict:
                return False
            else:
                notedict.append(sum)
            n = sum
        print(notedict)
        return True


pasum = 19
sol = Solution()
res = sol.isHappy(pasum)
print(res)