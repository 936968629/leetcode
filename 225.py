class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        length = len(self.queue)
        if length != 0:
            return self.queue.pop(length - 1)
        return []

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        length = len(self.queue)
        if length != 0:
            return self.queue[length - 1]
        return []

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()