from leetcode.public_class import ListNode
# class Solution:
#
#     count = 0
#
#     def visit(self,cur,pre,n):
#
#         if cur is None:
#             return
#         self.visit(cur.next,cur,n)
#         if self.count == n:
#             return
#         self.count += 1
#         if self.count == n:
#             pre.next = cur.next
#
#     def removeNthFromEnd(self, head, n: int):
#
#         if head is None:
#             return None
#
#         self.count = 0
#         index = ListNode(114514)
#         index.next = head
#         self.visit(index,None,n)
#
#         return index.next

class Solution:


    def removeNthFromEnd(self, head, n: int):

        if head is None:
            return None

        length = 0
        index = ListNode(114514)
        index.next = head
        probe = index
        while probe:
            probe = probe.next
            length += 1
        d_pos = length - n

        pos = 0
        pre,cur = index,index.next
        while pos != d_pos:
            pre = cur
            cur = cur.next
        pre.next = cur.next

        return index.next

