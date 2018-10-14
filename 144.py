class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # return [] if root is None else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        


