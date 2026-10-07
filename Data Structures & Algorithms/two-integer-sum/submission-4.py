class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] + (target - nums[i]) == target and (target - nums[i]) in nums[i+1:]:
                return [i, nums.index((target - nums[i]), i+1)]
        
