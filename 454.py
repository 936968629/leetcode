class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        find_map = {}
        for i in A:
            for j in B:
                if i+j in find_map.keys():
                    find_map[i+j] += 1
                else:
                    find_map[i+j] = 1
        res = 0
        for k in C:
            for l in D:
                if 0-k-l in find_map.keys():
                    res += find_map[0-k-l]

        print(find_map)
        print(res)
        return res


# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# A = [-1,-1]
# B = [-1,1]
# C = [-1,1]
# D = [1,-1]
A = [0,1,-1]
B = [-1,1,0]
C = [0,0,1]
D = [-1,1,1]
sol = Solution()
sol.fourSumCount(A, B, C, D)