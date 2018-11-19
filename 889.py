class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            length = len(pre)
            root = TreeNode(pre[0])
            root.left = self.constructFromPrePost(pre[1:post.index(pre[1])+2], post[:post.index(pre[1])+1])
            root.right = self.constructFromPrePost(pre[post.index(pre[1])+2:], post[post.index(pre[1])+1:length])
        return root


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
sol = Solution()
res = sol.constructFromPrePost(pre, post)
print(res)
