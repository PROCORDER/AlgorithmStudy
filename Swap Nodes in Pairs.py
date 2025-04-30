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
        if head is None or head.next is None:
            return head

        solution = head.next  # 최종 반환할 새로운 head

        def swapNumbers(first):
            if first is None:
                return None  # 더 이상 스왑할 쌍 없음
            elif first.next is None:
                return first

            node = first
            node, node.next, next = node.next, node, node.next.next
            node.next.next = swapNumbers(next)  # 핵심 수정 부분

            return node  # 현재 스왑된 노드 반환

        return swapNumbers(head)


a=ListNode(1,None)
a.next=ListNode(2,ListNode(3,ListNode(4)))
Solution=Solution()
Solution.swapPairs(a)
