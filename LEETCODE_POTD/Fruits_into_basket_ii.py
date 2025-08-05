class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        occupied=[False]*len(baskets)
        ct=0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j] and occupied[j]==False:
                    occupied[j]=True
                    ct+=1
                    break
        return len(fruits)-ct
        