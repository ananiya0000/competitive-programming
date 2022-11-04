# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=None
        fast=head
        while fast!=None and fast.next!=None:
            if(fast.val==fast.next.val):
                while fast.next!=None and fast.val==fast.next.val:
                    fast=fast.next
                if(slow!=None):
                    slow.next=fast.next
                    fast=fast.next
                else:
                    head=fast.next
                    fast=fast.next
            else:
                slow=fast
                fast=fast.next
        return head
