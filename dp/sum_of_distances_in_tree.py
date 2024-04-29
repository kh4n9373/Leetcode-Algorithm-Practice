from typing import List
from collections import defaultdict
def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    # I didn't come up with the solution by myself. 
    # I dont know how to update the sum of distance of the descendants of the root
    # after the first bfs.
    # The intuition behind the update is if we switch the right subtree to be the root
    # then every node of the right subtree will be closer 1 unit to the root,
    # while in other sides subtree (not right subtree) be furhter 1 unit to the root
    # so the update should be
    # new_sum_of_distances_from_root = current_sum_of_distances_from_root 
    #                                - number_of_nodes_of_chosen_subtree_to_be_new_root
    #                                + number_of_remaining_modes
    # To do so, we need or dfs
    dic = defaultdict(set)
    res = [0]*n
    count = [1]*n

    for edge in edges:
        dic[edge[0]].add(edge[1])
        dic[edge[1]].add(edge[0])
    
    def postOrder(root,parent):
        for i in dic[root]:
            if i != parent:
                postOrder(i,root)
                count[root] += count[i]
                res[root] += res[i] + count[i]
    def preOrder(root,parent):
        for i in dic[root]:
            if i != parent:
                res[i] = res[root] - count[i] + n - count[i]
                preOrder(i,root)
    postOrder(0,-1)
    preOrder(0,-1)
    return res
    