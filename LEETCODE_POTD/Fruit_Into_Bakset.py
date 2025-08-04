class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        mp={}
        i=0
        j=0
        res=0
        while(i<len(fruits)):
            mp[fruits[i]]=mp.get(fruits[i],0)+1
            if len(mp)>2:
                while len(mp)>2:
                    mp[fruits[j]]-=1
                    if mp[fruits[j]]==0:
                        del mp[fruits[j]]
                    j+=1
            res=max(res,i-j+1)
            i+=1
        return res
                