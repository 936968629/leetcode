# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        visited = {}  # original list nodes -> new list nodes
        dummy = RandomListNode(0)
        p_res = dummy

        p = head
        while p:
            if p in visited:
                p_res.next = visited[p]
            else:
                p_res.next = RandomListNode(p.label)
                visited[p] = p_res.next

            next_p_res = p_res.next
            if p.random in visited:
                next_p_res.random = visited[p.random]
            else:
                if p.random:
                    next_p_res.random = RandomListNode(p.random.label)
                    visited[p.random] = next_p_res.random

            p_res = p_res.next
            p = p.next

        return dummy.next
