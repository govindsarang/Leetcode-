class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l=len(nums)
        s=0
        for i in range(len(nums)):
            if l%(i+1)==0:
                s+=nums[i]**2
        return s


            
        