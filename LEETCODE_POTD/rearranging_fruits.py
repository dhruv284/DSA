class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """

        mp={}
        minele=float('inf')
        for i in range(len(basket1)):
            minele=min(basket1[i],minele)
            mp[basket1[i]]=mp.get(basket1[i],0)+1
        
        for i in range(len(basket2)):
            minele=min(basket2[i],minele)
            mp[basket2[i]]=mp.get(basket2[i],0)-1
        res=[]
        print(mp)
        for i in mp:
            ele=i
            count=abs(mp[i])
            if count==0:
                continue
            if count%2!=0:
                return -1
            for k in range((count//2)):
                res.append(ele)
        print(res)
        res.sort()

        ans=0
        for i in range(len(res)//2):
            ans+=min(minele*2,res[i])
        return ans