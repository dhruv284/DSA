class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        power=[]
        MOD=1e9+7
        for i in range(32):
            if n&(1<<i)!=0:
                power.append((2**i)%MOD)
        
        res=[]
        for i in queries:
            start=i[0]
            end=i[1]
            prod=1
            for k in range(start,end+1):
                prod=int((power[k]*prod)%MOD)
            res.append(prod)
        return res

        

