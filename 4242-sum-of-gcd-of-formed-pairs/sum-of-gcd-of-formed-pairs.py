class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mxi=0
        prefixgcd=[]
        for num in nums:
            if num>mxi:
                mxi=num
            prefixgcd.append(gcd(num,mxi))
        prefixgcd.sort()
        left=0
        right=len(prefixgcd)-1
        s=0
        while left<right:
            s+=gcd(prefixgcd[left],prefixgcd[right])
            left+=1
            right-=1
        return s
        



            

        