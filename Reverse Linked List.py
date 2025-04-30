from platform import python_revision


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        def reverse(node,prev=None):
            if node is None:
                return prev
            next,node.next=node.next,prev
            return reverse(next,node)
        return reverse(head)

