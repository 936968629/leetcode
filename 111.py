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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        if not root:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        """
        # 使用队/列栈
        if not root:
            return 0
        minHeight = 0
        queue = [root]
        while queue:
            minHeight += 1
            size = len(queue)
            while size > 0:
                item = queue.pop()
                if not item.left and not item.right:
                    return minHeight
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
                size -= 1
        return minHeight


root = MyTree.createTree()
sol = Solution()
res = sol.minDepth(root)
print(res)