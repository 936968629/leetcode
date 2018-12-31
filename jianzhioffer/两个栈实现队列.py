class Solution:
    stack1 = []
    stack2 = []
    def appendTail(self, k):
        self.stack1.append(k)

    def deleteHead(self):
        # 栈2为空，将栈1数据移入栈2
        if len(self.stack2) == 0:
            while self.stack1:
                item = self.stack1.pop()
                self.stack2.append(item)

        if len(self.stack2) == 0:
            return None
        return self.stack2.pop()


Solution().appendTail(1)
Solution().appendTail(3)
# Solution().appendTail(5)
print(Solution().deleteHead())
print(Solution().deleteHead())
print(Solution().deleteHead())