class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range (0,len(nums)):
            m=max(nums[:i+1])
            mi=min(nums[i:])
            diff=m-mi
            if diff<=k:
                return i
        return -1
                    
        