class Solution:
    def applyDiff2D(self, mat, opr):
        n = len(mat)
        m = len(mat[0])
        weight = [[0]*m for _ in range(n)]
        
        for it in opr:
            val, r1, c1, r2, c2 = it
            
            weight[r1][c1] += val
            if c2+1 < m:
                weight[r1][c2+1] -= val
            if r2+1 < n:
                weight[r2+1][c1] -= val
            if r2+1 < n and c2+1 < m:
                weight[r2+1][c2+1] += val
        
       
        for i in range(n):
            for j in range(1, m):
                weight[i][j] += weight[i][j-1]
      
        for j in range(m):
            for i in range(1, n):
                weight[i][j] += weight[i-1][j]
        

        for i in range(n):
            for j in range(m):
                mat[i][j] += weight[i][j]
        
        return mat
