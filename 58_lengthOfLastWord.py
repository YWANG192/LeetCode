class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if s=="" :
            return 0

        split_list=s.split()
        
        
        if len(split_list)==0:
            return 0
        
        last_word=split_list[-1]
        
        return len(last_word)
