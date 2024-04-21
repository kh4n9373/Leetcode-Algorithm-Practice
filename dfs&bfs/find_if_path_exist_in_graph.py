from collections import defaultdict
from typing import List
def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    dic = defaultdict(list)
    if not edges:
        return True
    for i,j in edges:
        dic[i].append(j)
        dic[j].append(i)
    visited = set()
    def dfs(v):
        visited.add(v)
        for nei in dic[v]:
            if nei == destination:
                return True
            if nei not in visited:
                if dfs(nei):
                    return True
        return False
    return dfs(source)
