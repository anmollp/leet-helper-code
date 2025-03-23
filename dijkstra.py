class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        adj = defaultdict(list)

         # Build adjacency list
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Store shortest time to each node
        shortest_time = [float("inf")] * n
        shortest_time[0] = 0 # Distance to source is 0
        # Number of ways to reach each node in shortest time
        path_count = [0] * n
        path_count[0] = 1 # 1 way to reach node 0

        # Min-Heap (priority queue) for Dijkstra
        min_heap = [(0, 0)]

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            # Skip outdated distances
            if curr_time > shortest_time[curr_node]:
                continue

            for nei, time in adj[curr_node]:
                # Found a new shortest path → Update shortest time and reset path count
                if curr_time + time < shortest_time[nei]:
                    shortest_time[nei] = curr_time + time
                    path_count[nei] = path_count[curr_node]
                    heapq.heappush(min_heap, (shortest_time[nei], nei))
                # Found another way with the same shortest time → Add to path count
                elif curr_time + time == shortest_time[nei]:
                    path_count[nei] = (path_count[nei] + path_count[curr_node]) % MOD
            
        return path_count[n - 1]
