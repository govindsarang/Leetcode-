class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=int(nums[i])
            s=0
            while n!=0:
                d=n%10
                s+=d
                n=n//10
            if s==i:
                return i
        return -1

         