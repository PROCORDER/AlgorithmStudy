import collections
from collections import deque
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list:deque()
        if not head:
            return True
        node=head
        while node is not None:
            list.append(node.val)
            node=node.next

        while len(list)>1:
            if list.popleft() !=list.pop():
                return False
        return True