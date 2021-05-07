class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # Boundary Case
        
        if numRows == 1 or numRows > len(s):
            
            return s
        
        # Array of Array
        res = []        
        for _ in range(numRows):
            res.append([])
        
        # Append c one by one
        direction = -1
        row = 0
        
        for c in s:
            
            res[row].append(c)
            
            if row == 0 or row == len(res) - 1: # need to change direction
                direction = direction * (-1)
            
            row = row + direction
        
        for i in range(len(res)):
            
            res[i] = ''.join(res[i])
        
        return ''.join(res)
