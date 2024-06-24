class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left>=right or head is None:
            return head

        result=head
        node=head
        startChangePoint=None
        endChangePoint=None

        i=1
        while head:
            if i==left-1:
                startChangePoint=head
                node=startChangePoint
            elif i==right+1:
                endChangePoint=head
            head = head.next
            i+=1

        prev=None
        if startChangePoint is not None:
            prev,node, prev.next  = node.next, node.next.next,endChangePoint
        else:
            prev, prev.next, node = node.next, node, node.next.next
            prev.next.next=endChangePoint



        i=0
        if startChangePoint is None:
           i=1
        while i<right-left and node is not None:
            prev,next,node=node,prev,node.next
            prev.next=next
            i+=1

        if startChangePoint is not None:
            startChangePoint.next=prev
            return result
        else:
            return prev

Solution = Solution()
##a=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
a=ListNode(1,ListNode(2,ListNode(3)))
##a=ListNode(3,ListNode(5,None))
Solution.reverseBetween(a,1,3)
