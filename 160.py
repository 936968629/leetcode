#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        find_map = set()
        cura = headA
        curb = headB
        while cura:
            find_map.add(cura)
            cura = cura.next

        while curb:
            if curb in find_map:
                return curb
            curb = curb.next

        return None