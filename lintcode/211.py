import collections
class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        # write your code here
        if A == B:
            return True
        if len(A) == len(B):
            listA = collections.Counter(A)
            listB = collections.Counter(B)
            return sorted(listA.items(), key=lambda x:x[0]) == sorted(listB.items(), key=lambda x:x[0])
        return False

str1 = 'abcd'
str2 = 'bcad'
sol = Solution()
res = sol.Permutation(str1, str2)
print(res)
