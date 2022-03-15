class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        M, N = len(mat), len(mat[0])
        
        if M*N != r*c:
            return mat
        
        res = []
        temp = []
        
        for i in range(M):
            for j in range(N):
                
                temp.append(mat[i][j])
                
                if len(temp) == c:
                    res.append(temp)
                    temp = []
        
        return res
