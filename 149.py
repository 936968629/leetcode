# Definition for a point.
import numpy
from fractions import Fraction
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # y = kx + b
    def _line(self, point1x, point1y, point2x, point2y):
        point1 = Point(point1x, point1y)
        point2 = Point(point2x, point2y)
        # 点相同
        if point1.x == point2.x and point1.y == point2.y:
            return 'same'
        # x轴相等
        elif point1.x == point2.x:
            k, b = 'x', ''
        # y轴相等
        elif point1.y == point2.y:
            k = 0
            b = point1.y
        else:
            # k = (y2 - y1) / (x2 - x1);
            k = numpy.float128((point2.y - point1.y)) / numpy.float128((point2.x - point1.x))
            b = point1.y - k * point1.x
        return str(k) + ',' + str(b)

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)
        find_point = {}
        res = 2
        for i in range(len(points)):
            find_point = {}
            for j in range(len(points)):
                if i == j: continue
                result = self._line(points[i][0], points[i][1], points[j][0], points[j][1])
                # print(result)
                # if result == 'same':
                #     res += 1
                if result in find_point:
                    find_point[result] += 1
                    if 'same' not in find_point.keys():
                        res = max(res, find_point[result] + 1)
                    else:
                        if result == 'same':
                            res = max(res, find_point[result] + 1)
                        else:
                            res = max(res, find_point[result] + find_point['same'] + 1)
                else:
                    find_point[result] = 1
            print(find_point)

        print(res)
        return res
    '''
    def test(self, points):
        if not points:
            return 0
        Max = 0
        for i, v in enumerate(points[:-1]):
            Dict = {}
            flag = 0
            for j, t in enumerate(points[i + 1:]):
                if t[0] == v[0] and t[1] == v[1]:
                    flag += 1
                    continue
                if v[1] - t[1] == 0:
                    k = 'C90'
                else:
                    k = (v[0] - t[0]) / (v[1] - t[1])
                if k in Dict:
                    Dict[k] += 1
                else:
                    Dict[k] = 1
            if not Dict.values():
                Max = max(flag, Max)
            else:
                Max = max(max(Dict.values()) + flag, Max)
        print(Dict)
        print(Max + 1)
        return Max + 1
    '''


parpoints = [[1, 1], [2, 2], [3, 3]]
# parpoints = [[1, 1], [1, 2], [2, 2]]
# parpoints = [[1,1],[1,1],[2,2],[2,2]]
# parpoints = [[1, 1], [1, 1], [1, 1]]
parpoints = [[0, 0], [94911151, 94911150], [94911152, 94911151]]
sol = Solution()
sol.maxPoints(parpoints)
# sol.test(parpoints)
print( str(Fraction(3 / 7)) )