class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    @staticmethod
    def createLinkedList(nums):
        length = len(nums)
        if length == 0:
            return False
        head = ListNode(nums[0])
        cur = head
        for i in range(1, length):
            cur.next = ListNode(nums[i])
            cur = cur.next
        return head

def printLinkedList(head):
    cur = head
    while cur != None:
        print(cur.val, end='->')
        cur = cur.next
    print('NUll')


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res = rescur = ListNode(-1)
        if k == 1:
            return head
        count = n = 0
        cur = splitHead = head
        remainNode = None
        while cur:
            if count == 0:
                splitHead = cur
            precur = cur
            cur = cur.next
            count += 1
            if count == k:
                # 翻转链表
                count = 0
                n = 1
                precur.next = None
                reverseNode, endNode = self.reverseLinkedList(splitHead)
                rescur.next = reverseNode
                rescur = endNode
                remainNode = cur
        if n == 0:
            return head
        rescur.next = remainNode
        printLinkedList(res.next)

    @staticmethod
    def reverseLinkedList(head):
        cur = head
        pre = None
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        return pre, head

nums = [1, 2, 3, 4, 5]
nums = [1]
l = MyLinkedList.createLinkedList(nums)
k = 3
sol = Solution()
res = sol.reverseKGroup(l, k)
