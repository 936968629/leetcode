# Definition for singly-linked list.
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
        for i in range(1, len(nums)):
            cur.next = ListNode(nums[i])
            cur = cur.next
        return head

def printLinkedList(head):
    cur = head
    while cur != None:
        print(cur.val, end='->')
        cur = cur.next
    print('Null')

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        """
        while head != None and head.val == val:
            delnode = head.next
            head = delnode
            delnode = None
        if head == None:
            return None
        cur = head
        while cur.next != None:
            if cur.next.val == val:
                # 删除节点
                delnode = cur.next
                cur.next = delnode.next
                delnode.next = None
            else:
                cur = cur.next
            return head
        """
        dummmyhead = ListNode(-1)
        dummmyhead.next = head
        cur = dummmyhead
        while cur.next != None:
            if cur.next.val == val:
                # 删除节点
                delNode = cur.next
                cur.next = delNode.next
                delNode = None
            else:
                cur = cur.next
        return dummmyhead.next


nums = [1, 1, 1, 1, 1]
l = MyLinkedList.createLinkedList(nums)
printLinkedList(l)

sol = Solution()
val = 1
res = sol.removeElements(l, val)
printLinkedList(res)