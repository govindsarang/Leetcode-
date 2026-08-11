class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i=1
        while i<len(nums) and nums[i]==nums[i-1]+1:
            i+=1
        ans=sum(nums[:i])
        s=set(nums)
        while ans in s:
            ans+=1
        return ans
        
            
            





            
        
        