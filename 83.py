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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummmyhead = ListNode(-1)
        dummmyhead.next = head
        cur = dummmyhead
        while cur.next != None:
            if cur.next.next != None and cur.next.val == cur.next.next.val:
                delNode = cur.next
                cur.next = delNode.next
                delNode = None
            else:
                cur = cur.next
        return dummmyhead.next

nums = [1, 1, 2, 3, 3, 3]
l = MyLinkedList.createLinkedList(nums)
sol = Solution()
res = sol.deleteDuplicates(l)
printLinkedList(res)