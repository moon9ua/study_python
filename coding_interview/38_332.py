from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start = "JFK"
        path = [start]
        # t_len = len(tickets)
        tickets.sort()
        def dfs(search: str, elems):
            # print (t_len, str, tickets)
            # if len(path) == t_len + 1:
            if len(path) == len(tickets) + 1:
                return
            for t in tickets:
                if t[0] == search:
                    # tickets.remove(t)
                    path.append(t[1])
                    dfs(t[1], tickets[:].remove(t))
                    # dfs(t[1], tickets.remove(t))
                    # path.pop()
                    # tickets.append(t)
        dfs(start, tickets)
        return path

sol = Solution()
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print (sol.findItinerary(tickets))