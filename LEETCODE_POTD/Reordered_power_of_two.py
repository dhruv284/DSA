class Solution(object):
    def getsortedstring(self,s):
        t=list(s)
        t.sort()
        return "".join(map(str,t))
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=self.getsortedstring(str(n))
        for i in range(30):
            if s==self.getsortedstring(str(1<<i)):
                return True
        return False
        