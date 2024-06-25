class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in table.values():
                stack.append(char)
            elif char in table.keys():
                if stack == [] or table[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []



