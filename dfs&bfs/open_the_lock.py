from typing import List

def openLock(deadends: List[str], target: str) -> int:
    if '0000' in deadends:
        return -1 
    def children(cand):
        res = []
        for i in range(len(cand)):
            child_plus = cand[:i] + str((int(cand[i]) + 1) %10) + cand[i+1:]
            res.append(child_plus)
            child_minus = cand[:i] + str((int(cand[i]) - 1 + 10) % 10) + cand[i+1:]
            res.append(child_minus)
        return res
    queue = []
    visited = set(deadends)
    queue.append(('0000',0))
    while queue:
        cand, turn = queue.pop(0)
        if cand == target:
            return turn 
        for child in children(cand):
            if child not in visited:
                visited.add(child)
                queue.append((child,turn+1))
    return -1
                

        