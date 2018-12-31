class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        direction = 0
        while queue:
            pres = []
            size = len(queue)
            while size > 0:
                item = queue.pop(0)
                if direction == 0:
                    pres.append(item.val)
                else:
                    pres.insert(0, item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
                size -= 1
            res.append(pres)
            direction = 1 if direction == 0 else 0
        return res


sol = Solution()
# sol.zigzagLevelOrder(root)