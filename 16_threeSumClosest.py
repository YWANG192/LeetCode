class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        if len(nums) <= 3:
            return sum(nums)
        
        nums.sort()
        res = sum(nums[:3])
        
        for i in range(len(nums)-2):
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                
                temp_sum = nums[i] + nums[l] + nums[r]
                
                temp_diff = abs(temp_sum - target)
                
                res_diff = abs(res - target)
                
                if temp_diff < res_diff:
                    res = temp_sum
                
                if temp_sum - target > 0:
                    r -=1
                
                if temp_sum - target <=0:
                    
                    l += 1
        
        return res
