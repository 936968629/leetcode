class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyTree:
    def createTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        return root

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = 0
        temp = root
        # get maxHeight of the tree
        while temp:
            height += 1
            temp = temp.left
        return self.count(root, height)

    def count(self, root, maxHeight):
        if root is None:
            return 0
        if root.left is None:
            return 1
        height = 0
        temp = root.left
        while temp:
            height += 1
            temp = temp.right
        if height == (maxHeight - 1):  # left tree is perfect at the lowest level
            return pow(2, height) + self.count(root.right, maxHeight - 1)
        else:  # right tree must be perfect at one level shallower
            return pow(2, height) + self.count(root.left, maxHeight - 1)


root = MyTree().createTree()
sol = Solution()
res = sol.countNodes(root)
print(res)