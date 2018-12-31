class Solution:
    def jian(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        products = [None] * 50
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4, length + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                # 思路：每次求解值时将其他小于需要求解的长度是都列出来放在一个数组里
                # 如：求长度为5，最优解数组里必须得有长度为1,2,3,4的最优解值
                # 注：此处使用列表保存最优解数组是为了性能优化，虽然递归求解也能解出，但会造成大量重复执行
                temp = products[j] * products[i - j]
                if temp > max:
                    max = temp
                products[i] = max
        return products[length]

num = 8
sol = Solution()
res = sol.jian(num)
print(res)