class Solution:
    def maxRectSum(self, mat):
        n = len(mat)
        m = len(mat[0])
        res = -float('inf')
        
        for left in range(m):
            vec = [0] * n
            for right in range(left, m):
                
                for i in range(n):
                    vec[i] += mat[i][right]
                
              
                max_ending_here = vec[0]
                max_so_far = vec[0]
                for i in range(1, n):
                    max_ending_here = max(vec[i], max_ending_here + vec[i])
                    max_so_far = max(max_so_far, max_ending_here)
                
                res = max(res, max_so_far)
        
        return res
