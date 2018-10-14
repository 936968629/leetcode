class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        length = len(self.stack)
        if length == 0:
            return []
        else:
            return self.stack.pop(length-1)

    def top(self):
        """
        :rtype: int
        """
        length = len(self.stack)
        if length == 0:
            return []
        else:
            return self.stack[length - 1]

    def getMin(self):
        """
        :rtype: int
        """
        length = len(self.stack)
        if length == 0:
            return None
        else:
            return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()