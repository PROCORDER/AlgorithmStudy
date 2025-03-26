# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        q=[]
        if not head:
            return True

        while head is not None:
            q.append(head.val)
            head=head.next

        while len(q)>1:
            if q.pop(0)!=q.pop():
                return False

        return True

