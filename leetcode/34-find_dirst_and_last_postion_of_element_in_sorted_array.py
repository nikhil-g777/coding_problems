class Solution:
    
    # Binary search helper function, the occurence flag determines first/last position of target
    def search(self, nums, target, occurence):
        
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start+end)//2
            
            # continuing the search if there's another occurence of target to the left of mid
            if nums[mid] > target or (occurence == 'first' and nums[mid] == target and mid!= 0 and nums[mid-1] == target):
                end = mid - 1
            # continuing the search if there's another occurence of target to the right of mid
            elif nums[mid] < target or (occurence == 'last' and nums[mid] == target and mid != len(nums) - 1 and nums[mid+1] == target):
                start = mid + 1
            else:
                return mid
        return -1
                
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        first = self.search(nums, target, 'first')
        last = self.search(nums, target, 'last')
        
        return [first, last]