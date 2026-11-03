class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])

        count = 0

        for j in range(cols):
            for i in range(rows - 1):
                if strs[i][j] > strs[i + 1][j]:
                    count += 1
                    break

        return count