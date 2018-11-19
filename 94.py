class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Command:
    def __init__(self, s, node):
        self.s = s
        self.node = node

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # 非递归
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


sol = Solution()
res = sol.inorderTraversal(root)
print(res)