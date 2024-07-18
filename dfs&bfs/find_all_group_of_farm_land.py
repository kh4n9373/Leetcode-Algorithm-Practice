from typing import List
def findFarmland(land: List[List[int]]) -> List[List[int]]:
    r,c = len(land), len(land[0])
    visited = set()
    res = []
    def find_group(i,j):
        if i >= r or j >= c or land[i][j] == 0:
            return (-1,-1)
        land[i][j] = 0
        final_row_of_i, final_col_of_i = find_group(i+1,j)
        final_row_of_j, final_col_of_j = find_group(i,j+1)

        final_row = max(final_row_of_i,final_row_of_j,i)
        final_col = max(final_col_of_i,final_col_of_j,j)

        return (final_row, final_col)
    for i in range(r):
        for j in range(c):
            if land[i][j] == 1:
                fin_i, fin_j = find_group(i,j)
                res.append([i,j,fin_i,fin_j])
    return res
        


    