class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        find_map = {}
        res = 0
        for i in range(len(points)):
            find_map = {}
            for j in range(len(points)):
                if j != i:
                    # dis = self._dis(points[i], points[j])
                    dis = (points[i][0] - points[j][0])**2 + (points[i][1]-points[j][1])**2
                    if dis in find_map.keys():
                        # res += find_map[dis]
                        find_map[dis] += 1
                    else:
                        find_map[dis] = 1
            # print(find_map)
            for k, v in find_map.items():
                if v > 1:
                    res += v * (v - 1)

        print(res)
        return res


paspoints = [[0, 0], [1, 0], [2, 0]]
sol = Solution()
sol.numberOfBoomerangs(paspoints)
