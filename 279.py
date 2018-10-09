class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        queuelist = []
        queuelist.append([n, 0])
        while queuelist:
            item = queuelist.pop(0)
            num = item[0]
            step = item[1]

            if num == 0:
                print(step)
                return step
            i = 1
            while num - i * i >=0:
                queuelist.append([num - i*i , step+1])
                i += 1
        """
        


sol = Solution()
sol.numSquares(13)