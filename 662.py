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
        # if not root:
        #     return 0
        maxWidth = 1
        queue = [ [root, 1] ]
        while queue:
            size = len(queue)
            maxWidth = max(maxWidth, queue[-1][1] - queue[0][1]+1)
            while size > 0:
                item = queue.pop(0)
                if item[0].left:
                    queue.append([item[0].left, 2*item[1] ])
                if item[0].right:
                    queue.append([item[0].right, 2*item[1]+1 ])
                size -= 1
        return maxWidth

        left = {}
        self.ans = 0
        self.helper(root, 0, 0, left)
        return self.ans

    def helper(self, root, pos, level, left):
        if root == None:
            return
        if level not in left:
            left[level] = pos
        self.ans = max(self.ans, pos - left[level] + 1)
        self.helper(root.left, 2 * pos + 1, level + 1, left)
        self.helper(root.right, 2 * pos + 2, level + 1, left)


root = MyTree.createTree()
sol = Solution()
res = sol.widthOfBinaryTree(root)
print(res)