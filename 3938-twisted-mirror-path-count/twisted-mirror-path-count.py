from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[i][j][0]: ways entering from left
        # dp[i][j][1]: ways entering from above
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # Start at (0, 0)
        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ways = 1
                else:
                    ways = (dp[i][j][0] + dp[i][j][1]) % MOD

                if grid[i][j] == 0:
                    # Empty cell: move right
                    if j + 1 < n:
                        dp[i][j + 1][0] = (
                            dp[i][j + 1][0] + ways
                        ) % MOD

                    # Empty cell: move down
                    if i + 1 < m:
                        dp[i + 1][j][1] = (
                            dp[i + 1][j][1] + ways
                        ) % MOD

                else:
                    # Mirror:
                    # Entering from left -> reflect down
                    if i + 1 < m:
                        dp[i + 1][j][1] = (
                            dp[i + 1][j][1] + dp[i][j][0]
                        ) % MOD

                    # Entering from above -> reflect right
                    if j + 1 < n:
                        dp[i][j + 1][0] = (
                            dp[i][j + 1][0] + dp[i][j][1]
                        ) % MOD

        return sum(dp[m - 1][n - 1]) % MOD