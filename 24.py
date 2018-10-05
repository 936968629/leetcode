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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(-1)
        dummyhead.next = head
        p = dummyhead

        while p.next and p.next.next:
            # 交换
            node1 = p.next
            node2 = p.next.next
            nextNode = node2.next

            node2.next = node1
            node1.next = nextNode
            p.next = node2

            p = node1

        return dummyhead.next

sum = [1, 2, 3, 4]
l = MyLinkedList.createLinkedList(sum)

sol = Solution()
res = sol.swapPairs(l)
printLinkedList(res)