class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return False
        return_data = 0
        i, j = 0, len(height) - 1
        while i < j:
            # 长度
            area_length = j - i
            # 高度
            area_height = min(height[i], height[j])
            return_data = max(return_data, area_height*area_length)
            if height[i] <= height[j]:
                i += 1
                continue
            if height[i] > height[j]:
                j -= 1
                continue
        print(return_data)
        return return_data


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
sol.maxArea(height=heights)
