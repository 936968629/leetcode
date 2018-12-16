# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.helper(root)
        return self.sum

    def helper(self, root):
        if not root:
            return

        if root.left and not root.left.left and not root.left.right:
            self.sum += root.left.val

        self.helper(root.left)
        self.helper(root.right)