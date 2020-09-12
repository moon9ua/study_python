import collections
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list) # 그래프 생성
        for u, v, w in times:
            graph[u].append((v, w)) # {현재 노드: (새 노드, 소요시간)}
        
        Q = [(0, K)] # (소요시간, 노드)
        times = {}

        while Q: # 큐에 경로들 쌓기
            now_time, now_node = heapq.heappop(Q)
            if now_node not in times:
                times[now_node] = now_time # times에 (노드, 최소 소요시간) 저장
                for new_node, new_time in graph[now_node]:
                    heapq.heappush(Q, (now_time + new_time, new_node)) # 큐에 새롭게 갈 수 있는 노드들 추가

        if len(times) != N:
            return -1
        return max(times.values())

sol = Solution()
times = [[3,1,5], [3,2,2], [2,1,2], [3,4,1], [4,5,1], [5,6,1], [6,7,1], [7,8,1], [8,1,1]]
N = 8
K = 3
print (sol.networkDelayTime(times, N, K))