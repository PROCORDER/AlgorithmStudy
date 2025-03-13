import re
import collections


class Solution(object):
    def mostCommonWord(self):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph ="Bob hit a ball, the hit BALL flew far after it was hit."
        banned=["hit"]
        words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        print(words)
        counts=collections.Counter(words)
        return counts.most_common(1)[0][0]
solution=Solution()
solution.mostCommonWord()