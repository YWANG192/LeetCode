class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
        
        my_dict = {}
        res = []
        
        for num in nums1:            
            if num not in my_dict:
                my_dict[num] = 0
            else:                
                my_dict[num]+= 1
        
        for num in nums2:
            if num in my_dict and my_dict[num]>=0:
                res.append(num)
                my_dict[num]-=1
        
        return res
