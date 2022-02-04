class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} # dictionary to store all numbers that were seen
        
        for i in range(len(nums)):
            if target - nums[i] in seen: # check if the num we're looking for ( target - current num ) is in the dict
                return [seen[target-nums[i]], i] # return if found
            
            seen[nums[i]] = i # add number to seen dict
        
        return
        