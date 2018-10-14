class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack:
            return self.stack.pop(0)
        return []

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack:
            return self.stack[0]
        return []

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(4)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()