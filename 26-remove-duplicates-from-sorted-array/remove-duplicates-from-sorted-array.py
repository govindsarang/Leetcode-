class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        left=1
        right=0
        i=0
        k=0
        while left<len(nums) :
            if nums[left]==nums[right]:
                nums[left]="_"
            else:
                right=left
            left+=1    
        while i<len(nums):
            if nums[i]!="_":
                nums[k]=nums[i]
                k+=1
            i+=1         
        return k 
        """
        c=0
        left=0
        right=1
        c=0
        if 9 in nums:
            c+=1
        while right<len(nums):
            if nums[left]==nums[right]:
                nums[right]="_"
            else:
                left=right
            right+=1
        i=0
        k=0
        while i<len(nums):
            if nums[i]!="_":
                nums[k]=nums[i]
                k+=1
            i+=1
        return k
        

            

        
            
            


        