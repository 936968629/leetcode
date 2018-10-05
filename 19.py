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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        length = 0
        lenHead = head
        while lenHead:
            lenHead = lenHead.next
            length += 1
        if n > length:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        j = 0
        while cur and cur.next:
            if length == n:
                cur.next = cur.next.next
                break
            if j == length - n:
                delNode = cur.next
                if delNode:
                    cur.next = delNode.next
                else:
                    cur.next = None
                delNode = None
                j += 1
            else:
                cur = cur.next
                j += 1
        return dummy.next
        """
        # 双指针
        dummyhead = ListNode(-1)
        dummyhead.next = head
        p =dummyhead
        q = dummyhead

        for i in range(n+1):
            q = q.next
        while q:
            p = p.next
            q = q.next

        delNode = p.next
        p.next = delNode.next
        delNode = None

        return dummyhead.next

nums = [1, 2]
l = MyLinkedList.createLinkedList(nums)
sol = Solution()
res = sol.removeNthFromEnd(l, 2)
printLinkedList(res)