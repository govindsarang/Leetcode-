class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        m=k
        while True:
            if m not in nums:
                return m
            m+=k
        
        
        