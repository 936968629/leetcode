# Definition for singly-linked list.
# 链表反转
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MylinkedList:
    @staticmethod
    def createLinkedList(nums):
        length = len(nums)
        if length == 0:
            return False
        head = ListNode(nums[0])
        cur = head
        for i in range(1, length):
            newNode = ListNode(nums[i])
            cur.next = newNode
            cur = cur.next
        return head


def printLinkedList(head):
    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next
    print('Null')


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        pre = None
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode

        return pre


nums = [1, 2, 3, 4, 5]
l = MylinkedList.createLinkedList(nums)
printLinkedList(l)
sol = Solution()
res = sol.reverseList(l)
printLinkedList(res)
