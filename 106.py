class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        else:
            length = len(inorder)
            root = TreeNode(postorder[length - 1])
            root.left = self.buildTree(inorder[:inorder.index(postorder[length - 1])],
                                       postorder[:inorder.index(postorder[length - 1])])
            root.right = self.buildTree(inorder[inorder.index(postorder[length - 1]) + 1:],
                                        postorder[inorder.index(postorder[length-1]):length])
        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
sol = Solution()
res = sol.buildTree(inorder, postorder)
print(res)
