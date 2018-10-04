# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList(object):
    """创建单链表"""
    @staticmethod
    def createLinkedList(nums, n):
        if n == 0:
            raise Exception('error')
        head = ListNode(nums[0])
        curnode = head
        for i in range(1, n):
            curnode.next = ListNode(nums[i])
            curnode = curnode.next
        # self._head = head
        return head

def printLinkedlist(head):
    curNode = head
    while curNode != None:
        print(curNode.val, end='->')
        curNode = curNode.next
    print('Null')

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # print(head.val)
        pre = None
        cur = head
        while cur != None:
            # 保存下一个节点
            nextNode = cur.next

            cur.next = pre

            pre = cur
            cur = nextNode
        return pre


data = [1, 2, 3, 4, 5]
l = MyLinkedList.createLinkedList(data, 5)
printLinkedlist(l)

sol = Solution()
res = sol.reverseList(l)
printLinkedlist(res)
