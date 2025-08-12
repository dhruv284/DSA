class Solution(object):
    def probability(self,A,B,dp):
        if A<=0 and B<=0:
            return 0.5
        if A<=0:
            return 1
        if B<=0:
            return 0
        if dp[A][B]!=-1:
            return dp[A][B]
        op1=self.probability(A-100,B-0,dp)
        op2=self.probability(A-75,B-25,dp)
        op3=self.probability(A-50,B-50,dp)
        op4=self.probability(A-25,B-75,dp)
        dp[A][B]=(op1+op2+op3+op4)*0.25
        return (op1+op2+op3+op4)*0.25
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n > 4800:  
            return 1.0
        dp=[]
        for i in range(n+1):
            a=[]
            for j in range(n+1):
                a.append(-1)
            dp.append(a)
        return (self.probability(n,n,dp))
        