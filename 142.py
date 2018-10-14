class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 使用set
        """
        find_map = set()
        iscycle = self.iscycle(head=head)
        if not iscycle:
            return None
        else:
            while True:
                if head not in find_map:
                    find_map.add(head)
                else:
                    return head
                head = head.next
        """
        # 不使用set
        slow = head
        iscycle, xiangyu = self.iscycle(head)
        if not iscycle:
            return None
        while slow and xiangyu:
            if slow == xiangyu:
                return xiangyu
            slow = slow.next
            xiangyu = xiangyu.next

    def iscycle(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True,slow
        return False,slow