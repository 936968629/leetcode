class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        res = self.findPath(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res

        preSum = {0: 1}

        def dfs(node, currSum, target, preSum):
            if not node:
                return 0

            currSum += node.val
            res = preSum.get(currSum - target, 0)

            preSum[currSum] = preSum.get(currSum, 0) + 1

            res += dfs(node.left, currSum, target, preSum) + dfs(node.right, currSum, target, preSum)

            preSum[currSum] -= 1

            return res

        return dfs(root, 0, sum, preSum)

    #找到包含root节点的路径
    def findPath(self, root, sum):
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.findPath(root.left, sum - root.val)
        res += self.findPath(root.right, sum - root.val)
        return res