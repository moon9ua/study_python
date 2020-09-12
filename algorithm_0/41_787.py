from typing import List
import collections
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w)) # 튜플로.

        q = [(0, src, 0)] # (시간, 위치, 경유지) # 좀 헷갈리네. -1이라고 해서 틀렸었음.

        # 내 답안
        # rets = []
        # while q:
        #     now_time, now_node, k = heapq.heappop(q)
        #     if k <= K:
        #         if now_node == dst:
        #             rets.append(now_time)
        #         for new_node, new_time in graph[now_node]:
        #             heapq.heappush(q, (now_time + new_time, new_node, k + 1))

        while q:
            now_time, now_node, k = heapq.heappop(q)
            if now_node == dst:
                return now_time
            if k <= K:
                for new_node, new_time in graph[now_node]:
                    heapq.heappush(q, (now_time + new_time, new_node, k + 1))

        return -1

sol = Solution()
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print (sol.findCheapestPrice(n, edges, src, dst, k))