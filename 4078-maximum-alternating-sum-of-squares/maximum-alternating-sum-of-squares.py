class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        score = 0

        for i in range(n):
            if i < (n + 1) // 2:
                score += nums[n - 1 - i] ** 2
            else:
                score -= nums[n - 1 - i] ** 2

        return score