class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        p1 = len(a) - 1
        p2 = len(b) - 1
        
        carry = 0
        res = ''
        
        while p1 >= 0 and p2 >=0:
            
            num1 = int(a[p1])
            num2 = int(b[p2])
            
            value = (num1 + num2 + carry) % 2
            carry = (num1 + num2 + carry) // 2            
            
            res = str(value) + res
            
            p1 -= 1         
            p2 -= 1
        
        while p1 >=0:
            
            num1 = int(a[p1])           
            value = (num1 + carry) % 2
            carry = (num1 + carry) // 2
            
            
            res = str(value) + res            
            p1 -= 1 
            
        
        while p2 >=0:
            
            num2 = int(b[p2])            
            value = (num2 + carry) % 2
            carry = (num2 + carry) // 2
            
            res = str(value) + res           
            p2 -= 1             
        
        if carry ==1:
            
            res = '1' + res
        
        return res
            
        
        
