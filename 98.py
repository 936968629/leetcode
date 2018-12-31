class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nums = self.inorder(root)
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                return False

        return True



    def inorder(self, root):
        if not root:
            return []
        res = []
        queue = []
        queue.append(['go', root])
        while queue:
            item = queue.pop()
            if item[0] == 'go':

                if item[1].right:
                    queue.append(['go', item[1].right])
                queue.append(['print', item[1].val])
                if item[1].left:
                    queue.append(['go', item[1].left])

            else:
                res.append(item[1].val)
        return res