class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyTree:
    def createTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        return root


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        if not root:
            return
        nodeLeft = [root.left]
        nodeRight = [root.right]
        while nodeLeft:
            nodeLeftNext = []
            nodeRightNext = []
            for i in range(len(nodeLeft)):
                if nodeLeft[i] and nodeRight[i]:
                    if nodeLeft[i].val != nodeRight[i].val:
                        return False
                    else:
                        nodeLeftNext.append(nodeLeft[i].left)
                        nodeLeftNext.append(nodeLeft[i].right)
                        nodeRightNext.append(nodeRight[i].right)
                        nodeRightNext.append(nodeRight[i].left)
                elif nodeLeft[i] or nodeRight[i]:
                    return False
            nodeLeft = nodeLeftNext
            nodeRight = nodeRightNext
        return True
        """
        if root:
            return self.isSymmetricTree(root.left, root.right)
        return True

    def isSymmetricTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(p.right, q.left)
        return p == q


root = MyTree().createTree()
sol = Solution()
res = sol.isSymmetric(root)
print(res)