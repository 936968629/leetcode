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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 获取链表长度
        if not head:
            return head
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        k = k % length
        if k == 0:
            return head
        # print(k)
        # 分割链表
        fast = cur = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            cur = cur.next
            fast = fast.next
        list2 = cur.next
        cur.next = None
        fast.next = head
        # printLinkedList(list2)
        return list2


nums = [1, 2, 3, 4, 5]
k = 2
l = MylinkedList.createLinkedList(nums)
# printLinkedList(l)
sol = Solution()
res = sol.rotateRight(l, k)



