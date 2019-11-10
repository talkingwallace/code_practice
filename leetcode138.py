"""

"""


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:

    def copyRandomList(self, head:Node) -> Node:

        if not head:
            return None
        # copy next
        probe = head
        while probe:
            new_node = Node(probe.val,probe.next,probe.random)
            probe.next = new_node
            probe = probe.next.next

        # copy random
        probe = head
        while probe:
            probe.next.random = probe.random.next
            probe = probe.next.next

        # extract
        new_head = Node()
        pre,cur = new_head,head.next
        while cur:
            pre.next = cur
            pre = cur
            if cur.next:
                cur = cur.next.next
            else:
                break

        return new_head.next