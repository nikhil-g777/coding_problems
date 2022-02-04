class Solution: 
    
    def reverse(self, nums, start, end): # helper function to reverse string
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return

        n = len(nums)
        k = k % n # optimize/reduce k because for every n rotations, array is back to original structure

        
        self.reverse(nums, 0 , n-1) # reverse entire list
        self.reverse(nums, 0, k-1) # reverse elements till k, these are the elemts displaced which will come to start of the list
        self.reverse(nums, k, n-1) # reverse elements from k to n
        
        return