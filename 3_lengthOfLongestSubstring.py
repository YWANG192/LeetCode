class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i = 0
        my_dict = {}
        max_len = 0
        
        
        
        for j in range(len(s)):
            
            if not s[j] in my_dict:
                
                my_dict[s[j]] = j
                
            else:
                
                if i < my_dict[s[j]] + 1:
                    i = my_dict[s[j]] + 1
                
                my_dict[s[j]] = j
                
            temp_len = j-i+1

            if temp_len > max_len:
                max_len = temp_len
                

        return max_len
