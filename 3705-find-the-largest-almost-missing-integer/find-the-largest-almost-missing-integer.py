class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l=len(nums)
        f={}
        for i in nums:
                if i in f:
                    f[i]+=1
                else:
                    f[i]=1
        if k==1:
            maxi=-1
            for i in nums:
                if f[i]==1:
                    maxi=max(i,maxi)
            return maxi
        elif k==l:
            return max(nums)
        else:
            a=nums[0]
            b=nums[l-1]
            if f[a]==1 and f[b]==1:
                return max(a,b)
            elif f[a]==1:
                return a
            elif f[b]==1:
                return b
            else:
                return -1
             
        