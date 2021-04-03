class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            
            return False
        
        c = x
        b = 0
        
        while c:
            b = b*10 + c%10
            c = c // 10
        
        return b == x
