class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters,digits=[],[]
        for log in logs:
            if log.split()[1][0].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))
        return letters+digits

solution=Solution()
solution.reorderLogFiles("a logs tew")