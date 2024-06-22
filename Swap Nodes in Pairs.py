class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node,result=head,None
        cur =ListNode(None)
        if head is None:
            return head
        elif  head.next is None:
            return head
        else:
            cur,cur.next,next1 = node.next,node,node.next.next
            result=cur
            cur=cur.next
            node=next1

        while node is not None:
            if node.next is not None:
                cur.next,cur.next.next,next1=node.next,node,node.next.next
                cur=cur.next.next
                node=next1
            elif node is not None:
                cur.next,next=node,node.next
                node=next
                cur=cur.next
        cur.next=None
        return result
a=ListNode(1,None)
a.next=ListNode(2,ListNode(3))
Solution=Solution()
Solution.swapPairs(a)
