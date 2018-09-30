class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        ans = 0
        l, r = 0, len(height) - 1
        while l < r and height[l] <= height[l + 1]:
            l += 1
        while l < r and height[r] <= height[r - 1]:
            r -= 1

        while l < r:
            left = height[l]
            right = height[r]
            if left <= right:
                #add volum until an edge larger than the left edge 添加体积直到边缘大于左边缘
                l += 1
                while l < r and left >= height[l]:
                    ans += left - height[l]
                    l += 1
            else:
                # add volum until an edge larger than the right volum
                r -= 1
                while l < r and height[r] <= right:
                    ans += right - height[r]
                    r -= 1
        print(ans)
        return ans


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = Solution()
sol.trap(heights)

