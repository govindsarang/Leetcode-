
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                result.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue

                new_str = curr[:i] + curr[i + 1:]

                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)

        return result
