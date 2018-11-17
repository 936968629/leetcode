class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Command:
    def __init__(self, s, node):
        self.s = s
        self.node = node

class MyTreeNode:
    @staticmethod
    def createTree():
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        return root

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        #使用非递归
        res = []
        stack = []
        stack.append(Command('go', root))
        while stack:
            item = stack.pop()
            if item.s == 'print':
                res.append(item.node.val)
            elif item.s == 'go':
                if not item.node:
                    continue
                if item.node.right:
                    stack.append(Command('go', item.node.right))
                stack.append(Command('print', item.node))
                if item.node.left:
                    stack.append(Command('go', item.node.left))
        return res


root = MyTreeNode.createTree()
sol = Solution()
sol.postorderTraversal(root)