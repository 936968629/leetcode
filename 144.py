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
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归
        """
        if root is None:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        """
        # 非递归 用栈实现
        res = []
        stack = []
        command = Command('go', root)
        stack.append(command)
        while stack:
            item = stack.pop()
            if item.s == 'print':
                res.append(item.node.val)
            elif item.s == 'go':

                stack.append(Command('print', item.node))
                if item.node.right:
                    stack.append(Command('go', item.node.right))
                if item.node.left:
                    stack.append(Command('go', item.node.left))
        return res

root = MyTreeNode.createTree()
sol = Solution()
res = sol.preorderTraversal(root)
print(res)

