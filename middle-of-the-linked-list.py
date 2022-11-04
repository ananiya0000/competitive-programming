# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i=head
        j=head.next
        while j is not None:
            i=i.next
            j=j.next
            if(j is not None):
                j=j.next
        return i
