class Solution:
    @staticmethod
    def func(z):
        try:
            z = int(z)
            return isinstance(z, int)
        except ValueError:
            return False

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) < 3:
            # if self.func(tokens)
            return int(tokens.pop())
        stack = []
        for item in tokens:
            if self.func(item):
                stack.append(item)
            else:
                firstItem = int(stack.pop())
                secondItem = int(stack.pop())
                if item == '/':
                    result = int(secondItem / firstItem)
                elif item == '*':
                    result = secondItem * firstItem
                elif item == '+':
                    result = secondItem + firstItem
                elif item == '-':
                    result = secondItem - firstItem
                stack.append(result)
        print(stack)
        return stack.pop()


# nums = ["4", "13", "5", "/", "+"]
nums = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# nums = [18]
nums = ["4", "13", "5", "/", "+"]
sol = Solution()
res = sol.evalRPN(nums)
print(res)
