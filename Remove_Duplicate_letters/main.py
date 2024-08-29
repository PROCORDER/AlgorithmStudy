
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()  # 이미 추가된 문자를 추적
        stack = []    # 결과를 저장할 스택
        last_occurrence = {c: i for i, c in enumerate(s)}  # 각 문자의 마지막 위치

        for i, c in enumerate(s):
            if c in seen:
                continue  # 이미 포함된 문자면 건너뛰기

            # 현재 문자가 스택의 마지막 문자보다 작고,
            # 마지막 위치가 현재 인덱스보다 큰 경우
            while stack and c < stack[-1] and last_occurrence[stack[-1]] > i:
                seen.remove(stack.pop())  # 스택에서 제거하고, seen에서 삭제

            seen.add(c)  # 현재 문자를 seen에 추가
            stack.append(c)  # 스택에 추가

        return ''.join(stack)




        return solution