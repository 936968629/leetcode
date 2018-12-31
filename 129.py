class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.helper(root, '')
        return self.sum

    def helper(self, root, item):
        if not root:
            return
        item += str(root.val)
        if not root.left and not root.right:
            self.sum += int(item)
            return

        self.helper(root.left, item)
        self.helper(root.right, item)