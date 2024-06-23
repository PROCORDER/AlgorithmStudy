# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd, Even = head, head.next
        Evenhead=Even
        result=odd
        while head:
            if Even.next and Even.next.next:
                odd.next, Even.next, head = Even.next, Even.next.next, Even.next.next.next
                odd,Even=odd.next,Even.next
            elif Even.next is None:
                break
            elif Even.next.next is None:
                odd.next=Even.next
                odd= odd.next
                break

        Even.next=None
        odd.next=Evenhead
        return result

Solution = Solution()
##a=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
a=ListNode(1,ListNode(1))
Solution.oddEvenList(a)



