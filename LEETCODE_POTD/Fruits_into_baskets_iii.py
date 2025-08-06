class Solution(object):
    def computeSegmentTree(self,i,l,r,segmentTree,baskets):
        if l==r:
            segmentTree[i]=baskets[l]
            return 
        mid=l+(r-l)//2
        self.computeSegmentTree(2*i+1,l,mid,segmentTree,baskets)
        self.computeSegmentTree(2*i+2,mid+1,r,segmentTree,baskets)
        segmentTree[i]=max(segmentTree[2*i+1],segmentTree[2*i+2])

    def querySegmentTree(self,i,l,r,segmentTree,val):
        if segmentTree[i]<val:
            return False
        if l==r:
            segmentTree[i]=-1
            return True
        mid=l+(r-l)//2
        placed=False
        if segmentTree[2*i+1]>=val:
            placed=self.querySegmentTree(2*i+1,l,mid,segmentTree,val)
        else:
            placed=self.querySegmentTree(2*i+2,mid+1,r,segmentTree,val)
        segmentTree[i] = max(segmentTree[2*i + 1], segmentTree[2*i + 2])
        return placed

    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n=len(fruits)
        segmentTree=[-1]*4*n
        self.computeSegmentTree(0,0,n-1,segmentTree,baskets)
        ct=0
        for fruit in fruits:
            if self.querySegmentTree(0,0,n-1,segmentTree,fruit)==False:
                ct+=1
        return ct
