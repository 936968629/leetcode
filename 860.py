class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] != 5:
            return False
        list_five = 1
        list_ten = 0
        list_twenty = 0
        list_money = [20, 10]
        for i in range(1, len(bills)):
            if bills[i] == 5:
                list_five += 1
            else:
                remain_money = bills[i] - 5



sol = Solution()
res = sol.lemonadeChange([])



# 钱找零 获取最少的数量
class Solution2:
    def lemonadeChange2(self, money):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count = 0
        logList = {}
        moneyList = [100, 50, 20, 10, 5, 1]
        for i in range(len(moneyList)):
            n = money // moneyList[i]
            if n > 0:
                money = money - n * moneyList[i]
                count += n
                logList[moneyList[i]] = n
        print(count)
        print(logList)


sol = Solution2()
res2 = sol.lemonadeChange2(582)