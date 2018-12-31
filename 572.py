class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if not t:
            return True
        return self.dfs(s, t)

    def dfs(self, s, t):
        if not s:
            return False

        if s.val == t.val and self.checkTree(s, t):
            return True

        return self.dfs(s.left, t) or self.dfs(s.right, t)

    def checkTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False

        if root1.val != root2.val:
            return False

        return self.checkTree(root1.left, root2.left) and self.checkTree(root1.right, root2.right)

