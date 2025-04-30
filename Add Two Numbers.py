# Definition for singly-linked list.
class ListNode(object):
       def __init__(self, val=0, next=None):
           self.val = val
           self.next = next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        up=0
        sum=0
        solution=ListNode()
        solution_head=solution
        while l1  or l2 or up:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum=val1+val2+up

            up=0

            if sum>=10:
                up=1
                sum-=10
            solution.next= ListNode(sum, None)
            solution=solution.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return solution_head.next

# 헬퍼 함수: 리스트를 연결리스트로 변환
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 헬퍼 함수: 연결리스트를 리스트로 변환
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# 테스트용 입력
l1 = list_to_linkedlist([2, 4, 3])  # 342
l2 = list_to_linkedlist([5, 6, 4])  # 465

# 계산 수행
sol = Solution()
result_node = sol.addTwoNumbers(l1, l2)

# 결과 출력
print(linkedlist_to_list(result_node))
