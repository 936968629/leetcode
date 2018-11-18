class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(preorder[0])
        else:
            flag = TreeNode(preorder[0])
            flag.left = self.buildTree(preorder[1:inorder.index(preorder[0])+1], inorder[:inorder.index(preorder[0]) ])
            flag.right = self.buildTree(preorder[inorder.index(preorder[0])+1:], inorder[inorder.index(preorder[0])+1:])
        return flag


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
sol = Solution()
res = sol.buildTree(preorder, inorder)
