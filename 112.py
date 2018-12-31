class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        res = self.helper(root, sum, 0)
        if res is True:
            return True
        return False

    def helper(self, root, sum, now):
        if not root:
            return
        val = root.val
        now += val
        if not root.left and not root.right and now == sum:
            return True
        leftres = self.helper(root.left, sum, now)
        rightres = self.helper(root.right, sum, now)
        now -= val
        if leftres is True or rightres is True:
            return True
        return False
