class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for x in pushed:

            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return stack == []


pushed = [1,2,3,4,5]
# popped = [4,5,3,2,1]
popped = [4,3,5,1,2]
sol = Solution()
res = sol.validateStackSequences(pushed, popped)
print(res)