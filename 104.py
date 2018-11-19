class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyTree:
    @staticmethod
    def createTree():
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(5)
        root.left.left.left.left = TreeNode(6)
        root.left.left.left.left.left = TreeNode(7)
        return root


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftMax = self.maxDepth(root.left) + 1
        rightMax = self.maxDepth(root.right) + 1
        return max(leftMax, rightMax)


root = MyTree.createTree()
sol = Solution()
res = sol.maxDepth(root)
print(res)