class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == None:
            
            return []
        
        my_dict = {}
        
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[target - nums[i]] = i
            else:
                return [i, my_dict[nums[i]]]
