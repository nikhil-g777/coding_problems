class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        result = nums[0]
        current_sum = nums[0]
        
        # Kadanes Algorithm
        for num in nums[1:]:
            if current_sum + num > num: # add num to the sum if it increases the current sum
                current_sum = current_sum + num
            else: # take only the num if current sum + num is less than the num itself
                current_sum = num
            result = max(result, current_sum) # update result
        return result