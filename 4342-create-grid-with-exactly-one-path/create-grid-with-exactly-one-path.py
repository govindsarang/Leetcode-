class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Initialize an m x n grid filled with obstacles '#'
        grid = [['#'] * n for _ in range(m)]
        
        # Fill the first column with free cells '.'
        for r in range(m):
            grid[r][0] = '.'
            
        # Fill the last row with free cells '.'
        for c in range(n):
            grid[m - 1][c] = '.'
            
        # Join each row list into a string
        return ["".join(row) for row in grid]