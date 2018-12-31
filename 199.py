class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            pre = []
            while size > 0:
                item = queue.pop(0)
                pre.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
                size -= 1
            res.append(pre)
        resData = []
        for preitem in res:
            resData.append(preitem.pop())
        return resData
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            res.append(queue[-1].val)
            while size > 0:
                item = queue.pop(0)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
                size -= 1
        return res