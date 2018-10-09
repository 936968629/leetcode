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
            cur.next = ListNode(nums[i])
            cur = cur.next
        return head

def printLinkedList(head):
    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next
    print('Null')

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head and not head.next:
            return
        # 从中间分割成两个链表
        bianli= list1 = head
        fasterbianli = head
        prebianli = None
        newhead = cur = ListNode(-1)
        newhead.next = head
        # 找到中间元素
        while fasterbianli and fasterbianli.next:
            prebianli = bianli
            bianli = bianli.next
            fasterbianli = fasterbianli.next.next
        if not prebianli:
            return head
        list2 = prebianli.next
        prebianli.next = None
        # 翻转list2
        list2 = self.reverseList(list2)
        # printLinkedList(list1)
        # printLinkedList(list2)

        head = self._mergeLists(list1, list2)
        return head

    @staticmethod
    def reverseList(head):
        cur = head
        pre = None
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        return pre

    @staticmethod
    def _mergeLists(list1, list2):
        head = cur = ListNode(-1)
        while list1 and list2:
            cur.next = list1
            cur = cur.next
            if list1 and list1.next:
                list1 = list1.next
            else:
                list1 = None
            cur.next = list2
            if list2 and list2.next:
                list2 = list2.next
            else:
                list2 = None
            cur = cur.next
        return head.next


nums = [1, 2, 3, 4]
# nums = [1]
l = MylinkedList.createLinkedList(nums)
# printLinkedList(l)
sol = Solution()
res = sol.reorderList(l)
printLinkedList(res)