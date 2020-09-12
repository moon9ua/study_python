# 재귀
# from typing import List
# import collections
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = collections.defaultdict(list)
#         for a, b in sorted(tickets):
#             graph[a].append(b)
#         route = []
#         def dfs(a):
#             print ("현재:", a)
#             while graph[a]:
#                 dfs(graph[a].pop(0))
#             route.append(a)
#         dfs("JFK")
#         return route[::-1]

# 반복
from typing import List
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route, stack = [], ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append()


sol = Solution()
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print (sol.findItinerary(tickets))