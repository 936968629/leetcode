from collections import deque
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
        root.left.right = TreeNode(5)
        return root

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        q, result = deque(), []
        if root:
            q.append(root)
        while len(q):
            level = []
            for _ in range(len(q)):
                x = q.popleft()
                level.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            result.append(level)
        return result
        """
        if not root: return []
        stack, queue, res, nCount = [root], [], [[root.val]], 1
        while stack:
            temp = stack.pop(0)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            nCount -= 1
            if nCount == 0:
                queue = [x.val for x in stack]
                res += [queue] if queue else []
                nCount = len(stack)
        return res


l = MyTree.createTree()
sol = Solution()
sol.levelOrder(l)