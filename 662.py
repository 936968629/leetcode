class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyTree:
    @staticmethod
    def createTree():
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(9)
        root.left.left.left = TreeNode(6)
        return root

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        width = 1
        queue = [root]
        while queue:
            size = len(queue)
            while size > 0:
                item = queue.pop(0)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
                size -= 1
            width = max(width, len(queue))
        return width


root = MyTree.createTree()
sol = Solution()
res = sol.widthOfBinaryTree(root)
print(res)