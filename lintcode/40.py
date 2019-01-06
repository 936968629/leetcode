class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.stack1.append(element)


    """
    @return: An integer
    """

    def pop(self):

        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


    """
    @return: An integer
    """

    def top(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[len(self.stack2)-1]



