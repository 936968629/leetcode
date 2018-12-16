# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class myTree:

    def createTree(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        return root

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = []
        if not root:
            return self.result
        self.helper(root, sum, 0, [])

        return self.result

    def helper(self, root, sum, now, item):
        if not root:
            return
        now += root.val
        item.append(root.val)
        if not root.left and not root.right and now == sum:
            self.result.append(item[:])
            item.pop()
            return
        self.helper(root.left, sum, now, item)
        self.helper(root.right, sum, now, item)
        now -= root.val
        item.pop()


root = myTree().createTree()
sol = Solution()
res = sol.pathSum(root, 22)
print(res)