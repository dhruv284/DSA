MOD = 10**9 + 7

class Solution(object):
    

    def solve(self, n, num, x,dp):
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        currPowerValue = num ** x
        if currPowerValue > n:
            return 0
        
        if dp[n][num] != -1:
            return dp[n][num]
        
        take = self.solve(n - currPowerValue, num + 1, x,dp)
        skip = self.solve(n, num + 1, x,dp)
        
        dp[n][num] = (take + skip) % MOD
        return dp[n][num]

    def numberOfWays(self, n, x):
        
        dp = [[-1] * 301 for _ in range(301)]
        return self.solve(n, 1, x,dp)
