class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        path = ''
        self.helper(root, res, path)
        return res


    def helper(self, root, res, path):
        if not root:
            return
        if path == '':
            path = str(root.val)
        else:
            path = path + '->' + str(root.val)
        if not root.left and not root.right:
            res.append(path)
        else:
            self.helper(root.left, res, path)
            self.helper(root.right, res, path)
