class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.stack.append(number)
        if len(self.minStack) != 0:
            item = self.minStack[len(self.minStack)-1]
            if item <= number:
                self.minStack.append(item)
            else:
                self.minStack.append(number)
        else:
            self.minStack.append(number)

    """
    @return: An integer
    """

    def pop(self):
        if len(self.stack) == 0:
            return None
        self.minStack.pop()
        return self.stack.pop()


    """
    @return: An integer
    """

    def min(self):
        if len(self.minStack) == 0:
            return None
        return self.minStack[len(self.minStack)-1]


sol = MinStack()
sol.push(1)
print(sol.min())
# sol.pop()
sol.push(2)
print(sol.min())
sol.push(3)
print(sol.min())
sol.push(1)
sol.min()
