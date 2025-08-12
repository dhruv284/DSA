class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%2==0 and n!=0:
            return Solution.isPowerOfTwo(self,n/2)
        elif n==1:
            return True
        else:
            return False
       
        