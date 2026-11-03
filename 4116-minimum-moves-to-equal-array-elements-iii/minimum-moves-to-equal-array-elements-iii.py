class Solution:
    def minMoves(self, nums: list[int]) -> int:
        max_val = max(nums)
        moves = 0

        for num in nums:
            moves += max_val - num

        return moves