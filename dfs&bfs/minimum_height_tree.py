from typing import List 
from collections import defaultdict 

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    dic = defaultdict(list)
    for edge in edges:
        dic[edge[0]].append(edge[1])
        dic[edge[1]].append(edge[0])
    
    nei_count = {}
    leaves = []
    for node,nei in dic.items():
        if len(nei) == 1:
            leaves.append(node)
        nei_count[node] = len(nei)
    while leaves:
        if n <= 2:
            return list(leaves)
        for i in range(len(leaves)):
            leave = leaves.pop(0)
            n -= 1
            for nei in dic[leave]:
                nei_count[nei] -= 1
                if nei_count[nei] == 1:
                    leaves.append(nei)
                






        
            