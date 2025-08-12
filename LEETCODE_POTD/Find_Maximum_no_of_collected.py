class Solution(object):
    def child3collect(self,i,j,fruits,dp):
        if i<0 or i>len(fruits)-1 or j<0 or j>len(fruits)-1:
            return 0
        if i==len(fruits)-1 and j==len(fruits)-1:
            return 0
        if i<=j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        upright=fruits[i][j]+self.child3collect(i-1,j+1,fruits,dp)
        right=fruits[i][j]+self.child3collect(i,j+1,fruits,dp)
        bottomright=fruits[i][j]+self.child3collect(i+1,j+1,fruits,dp)
        dp[i][j]=max(upright,right,bottomright)
        return max(upright,right,bottomright)
    def child2collect(self,i,j,fruits,dp):
        if i<0 or i>len(fruits)-1 or j<0 or j>len(fruits)-1:
            return 0
        if i==len(fruits)-1 and j==len(fruits)-1:
            return 0
        if i>=j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        bottomleft=fruits[i][j]+self.child2collect(i+1,j-1,fruits,dp)
        bottomdown=fruits[i][j]+self.child2collect(i+1,j,fruits,dp)
        bottomright=fruits[i][j]+self.child2collect(i+1,j+1,fruits,dp)
        dp[i][j]=max(bottomleft,bottomdown,bottomright)
        return max(bottomleft,bottomdown,bottomright)
    def maxCollectedFruits(self, fruits):
        """
        :type fruits: List[List[int]]
        :rtype: int
        """
        res=0
        for i in range(len(fruits)):
            res+=fruits[i][i]
        n=len(fruits)
        dp1=[]
        for i in range(n):
            t=[]
            for j in range(n):
                t.append(-1)
            dp1.append(t)
        dp2=[]
        for i in range(n):
            t=[]
            for j in range(n):
                t.append(-1)
            dp2.append(t)
        res+=self.child2collect(0,len(fruits)-1,fruits,dp1)
        res+=self.child3collect(len(fruits)-1,0,fruits,dp2)
        return res

        