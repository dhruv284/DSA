

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            res=[[1],[1,1]]

            for i in range(1,numRows-1):
                
                l=[1]
                for j in range(len(res[i])-1):
                    l.append(res[i][j]+res[i][j+1])
                l.append(1)
                res.append(l[:])
            return res
        