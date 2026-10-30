
from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[node][count]
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        # Starting node contributes its label.
        if k < 1:
            return -1

        dist[0][1] = 0

        # (cost, node, consecutive_count)
        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            # Skip outdated states
            if cost != dist[u][count]:
                continue

            # Destination reached optimally
            if u == n - 1:
                return cost

            for v, w in adj[u]:

                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_dist = cost + w

                if new_dist < dist[v][new_count]:
                    dist[v][new_count] = new_dist
                    heapq.heappush(
                        pq,
                        (new_dist, v, new_count)
                    )

        return -1
