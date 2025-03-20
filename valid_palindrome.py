class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clist=[str.lower() for str in s if str.isalpha() or str.isnumeric()]
        len=clist.__len__()
        start=0
        end=len-1
        for i in range(len):
            if clist[start]!=clist[end]:
                return False
            start+=1
            end-=1


        return True

solution=Solution()
print(solution.isPalindrome("0P"))