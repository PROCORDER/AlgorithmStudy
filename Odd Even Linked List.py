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
        head=head.next.next
        Even_head=Even
        result=odd
        while head:
            odd.next=head
            odd=odd.next
            if head.next:
                Even.next=head.next
                Even=Even.next
            else:
                Even.next=None
                break
            head=head.next.next

        odd.next=Even_head
        return result

Solution = Solution()
a=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
#a=ListNode(1,ListNode(1))
Solution.oddEvenList(a)



