class Solution:
    def reverse(self, x: int) -> int:
        
        
        # For Python
        def divide (number, divider):
            return int (number * 1.0 / divider)
        
        def mode (number, m):
            if number < 0:
                return number % -m
            return number % m
        
        
        MAX = 2**31 - 1  #2147483647
        MIN = -2**31     # -2147483648
        
        res = 0
        
        while x:
            pop = mode(x, 10)
            x = divide(x, 10)
            
            if res > divide(MAX, 10) or (res == divide(MAX, 10) and pop > mode(MAX, 10)):
                return 0
            if res < divide(MIN, 10) or (res == divide(MIN, 10) and pop < mode(MIN, 10)):
                return 0
            
            res = res * 10 + pop
        
        return res
        
