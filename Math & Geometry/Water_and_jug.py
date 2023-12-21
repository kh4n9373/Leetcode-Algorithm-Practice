class Solution:
    def canMeasureWater(self, v1, v2, tar):
        if v1 + v2 < tar:
            return False
        state = [v1,v2,0]
        limit = [v1,v2,9999]
        best = float('inf')
        def pour(i,j,state_0):
            state = state_0.copy()
            a = min(limit[j]-state[j],state[i])
            state[i] = state[i] - a
            state[j] = state[j] + a
            return(state)
        def can_pour(state):
            a,b,c = state
            res = []
            if state[0] != 0 and state[1] != limit[1]:
                res.append(pour(0,1,state))
            if state[0] != 0 and state[2] != limit[2]:
                res.append(pour(0,2,state))
            if state[1] != 0 and state[0] != limit[0]:
                res.append(pour(1,0,state))
            if state[1] != 0 and state[2] != limit[2]:
                res.append(pour(1,2,state))
            if state[2] != 0 and state[1] != limit[1]:
                res.append(pour(2,1,state))
            if state[2] != 0 and state[0] != limit[0]:
                res.append(pour(2,0,state))
            return res
        queue = [(state,0)]
        explored = {tuple(state)}
        it = 0
        while queue:
            new_state,count = queue.pop(0)
            if tar in new_state:
                return True
                break
            for new_new_state in can_pour(new_state):
                if tuple(new_new_state) not in explored:
                    queue.append((new_new_state,count+1))
                    explored.add(tuple(new_new_state))
        if not queue:
            return False