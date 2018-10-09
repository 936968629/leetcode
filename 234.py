class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList():
    @staticmethod
    def createLinkedList(nums):
        length = len(nums)
        if length == 0:
            return False
        head = cur = ListNode(nums[0])
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        fast = head
        slow = head
        while fast and fast.next:
            prevslow = slow
            slow = slow.next
            fast = fast.next.next
        middle = prevslow.next
        prevslow.next = None
        # printLinkedList(head)
        # printLinkedList(middle)
        reverseMiddle = self._reverseLinked(middle)
        # printLinkedList(reverseMiddle)
        while head or reverseMiddle:
            if not head:
                return True
            if head.val != reverseMiddle.val:
                return False
            head = head.next
            reverseMiddle = reverseMiddle.next
        return True

    @staticmethod
    def _reverseLinked(head):
        cur = head
        pre = None
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        return pre

# nums = [1, 2, 2, 1]
# nums = []
nums = [1, 2, 1]
l = MyLinkedList.createLinkedList(nums)
# printLinkedList(l)
sol = Solution()
res = sol.isPalindrome(l)
print(res)