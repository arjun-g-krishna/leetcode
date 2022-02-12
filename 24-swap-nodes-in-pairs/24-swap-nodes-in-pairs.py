# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head is not None and head.next is not None:
            head.next.val,head.val=head.val,head.next.val
            head.next.next=self.swapPairs(head.next.next)
        return head    