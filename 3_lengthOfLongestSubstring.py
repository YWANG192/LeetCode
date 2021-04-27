class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        my_dict = {}
        max_len = 0
        
        for i in range (len(s)):
            
            if not s[i] in my_dict:
                
                my_dict[s[i]] = i
                
            else:
                
                if j < my_dict[s[i]] + 1:
                    j =  my_dict[s[i]] + 1
                
                my_dict[s[i]] = i
            
            temp_len = i - j + 1
            
            if temp_len > max_len:
                
                max_len = temp_len
        
        return max_len
            
