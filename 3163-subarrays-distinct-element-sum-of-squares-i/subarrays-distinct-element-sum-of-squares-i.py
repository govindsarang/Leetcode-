class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l=len(nums)
        res=0
        for i in range(l):
            seen=set()
            for j in range(i,l):
                seen.add(nums[j])
                count=len(seen)
                res+=count**2
        return res
        