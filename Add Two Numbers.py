# Definition for singly-linked list.
class ListNode(object):
       def __init__(self, val=0, next=None):
           self.val = val
           self.next = next
class Solution(object):
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            Sum=0
            head=ListNode(-1)
            result=head
            while l1 or l2:
                dum=0
                Sum=(l1.val+l2.val)
                if Sum>=10:
                    dum=1
                    Sum%=10
                if head.val==-1:
                    head.val=Sum
                else:
                    head.next=ListNode(Sum)
                    head = head.next
                if  l1.next  and  l2.next:
                    l1,l2=l1.next,l2.next
                    l1.val+=dum
                elif not l2.next and not l1.next:
                    if dum!=0:
                        head.next=ListNode(dum)
                    break
                elif not l2.next:
                    l1=l1.next
                    l2.val=0
                    l1.val+=dum
                elif not l1.next:
                    l2=l2.next
                    l1.val=0
                    l2.val+=dum
            return result

# 연결 리스트 초기화
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution=Solution()
result=solution.addTwoNumbers(l1,l2)
