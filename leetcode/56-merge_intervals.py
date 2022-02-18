class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return
        
        intervals.sort(key = lambda x : x[0]) # sort based on start value
        
        res = []
        n = len(intervals)
        
        for interval in intervals:
            if not res or res[-1][1] < interval[0]: # non-overlapping
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1]) # overlapping so extend the current end
        
        return res