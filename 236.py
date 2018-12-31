class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyTree:
    def createTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        return root


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.result = []
        self.preorder(root, p, [], 0)
        self.preorder(root, q, [], 0)
        # print(self.result)
        if self.result[0] and self.result[1]:
            i = 0
            while i < min(len(self.result[0]), len(self.result[1])):
                if self.result[0][i].val != self.result[1][i].val:
                    break
                i+=1
            return self.result[0][i-1]
        return None

    def preorder(self, root, search, item, isfinish):
        if not root or isfinish == 1:
            return
        item.append(root)
        if search.val == root.val:
            isfinish = 1
            self.result.append(item[:])
        self.preorder(root.left, search, item, isfinish)
        self.preorder(root.right, search, item, isfinish)
        item.pop()

    """
    # 网上解法
    if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left_ances = self.lowestCommonAncestor(root.left, p, q)
        right_ances = self.lowestCommonAncestor(root.right, p, q)
        if left_ances and right_ances:
            return root
        elif left_ances:
            return left_ances
        else:
            return right_ances
    """

root = MyTree().createTree()
sol = Solution()
res = sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(3))
print(res)