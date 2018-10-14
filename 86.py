class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smallhead = ListNode(-1)
        bighead = ListNode(-1)
        smallres = smallhead
        bigres = bighead
        cur = head
        while cur:
            if cur.val < x:
                smallhead.next = cur
                smallhead = smallhead.next
                # smallhead.next = None
            else:
                bighead.next = cur
                bighead = bighead.next
                # bighead.next = None
            cur = cur.next
        smallhead.next = bigres.next
        bighead.next = None
        return smallres.next