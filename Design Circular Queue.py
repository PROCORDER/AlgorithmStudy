class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.cq=[None]*k
        self.length=k
        self.fi=0
        self.li=0
    def cirCular(self,k):
        if k>=self.length:
            return 0
        elif k<0:
            return self.length-1
        else:
            return k



    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.cq[self.li]==None:
            self.cq[self.li]=value
            return True

        self.li = self.cirCular(self.li+1)
        if self.li==self.fi:
            self.li=self.cirCular(self.li-1)
            return False

        if self.li>=self.length:
            if self.cq[0]==None:
                self.li=0
                self.cq[self.li] = value
                return True
            else:
                self.li=self.cirCular(self.li - 1)
                print("더이상 들어갈 공간이 없습니다.")
                return False
        else:
            self.cq[self.li]=value
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.cq[self.fi]==None:
            return False
        self.cq[self.fi] = None
        if self.fi==self.li:
            return True

        self.fi=self.cirCular(self.fi+1)
        return True

    def Front(self):
        """
        :rtype: int
        """
        if  self.cq[self.fi]!=None:
            return  self.cq[self.fi]
        else:
            return -1

    def Rear(self):
        """
        :rtype: int
        """
        if  self.cq[self.li]!=None:
            return  self.cq[self.li]
        else:
            return -1


    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.li==self.fi and self.cq[self.fi]==None:
            return True
        else:
            return False


    def isFull(self):
        """
        :rtype: bool
        """
        checkli=self.cirCular(self.li+1)
        if self.fi==checkli:
            return True
        else:
            return False


obj = MyCircularQueue(6)

obj.enQueue(3)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(4)
obj.deQueue()
obj.enQueue(4)

print(obj.Rear())
print(obj.Rear())

# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()