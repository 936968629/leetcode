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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dumm = ListNode(0)
        dumm.next = head
        pre = dumm
        for i in range(m-1):
            pre = pre.next

        reverse = None
        cur = pre.next
        for i in range(n-m+1):
            nextNode = cur.next
            cur.next = reverse
            reverse = cur
            cur = nextNode

        pre.next.next = cur
        pre.next = reverse

        return dumm.next


nums = [1, 2, 3, 4, 5]
l = MyLinkedList.createLinkedList(nums)
printLinkedList(l)

m = 2
n = 4
sol = Solution()
res = sol.reverseBetween(l, m, n)
printLinkedList(res)