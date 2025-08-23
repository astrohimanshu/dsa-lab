#%%
import numpy as np
from tabulate import tabulate
#%%
def forward_elimination(A, b):

    m, n = len(A), len(A[0])    
    #augemented matrix [A b]

    Ab = [A[i] + [b[i]] for i in range(m)] 

    current_row = 0
    pivots = {}
    free_cols = []
    for current_col in range(n):
        # pivot is somewhere on this column so we move down column col, fix the col iterate over rows downwards untill non zero pivot found
        for row in range(current_row, m):
            pivot = None
            if Ab[row][current_col] != 0:
                # pivot found 
                pivot = Ab[row][current_col]
                pivots[(current_row, current_col)] = pivot

                # swap with current_row 
                Ab[current_row] , Ab[row] = Ab[row], Ab[current_row]

                # now pivot is at current_row,current_col at correct place

                # normalize the pivot_row swapped with current, also divide uptill b so n + 1
                Ab[current_row] = [ x / Ab[current_row][current_col] for x in Ab[current_row] ]
                
                # subtract whole row below pivots row after multiplying by that rows element along the pivot column
                for i in range(current_row + 1, m):
  
                    Ab[i] = [ Ab[i][j] - Ab[current_row][j] * Ab[i][current_col] for j in range(n + 1) ]

            # if pivot is found increment rows, if pivot is not found we move to next column but from same row
            if pivot != None:
                current_row += 1

        # maybe we found the pivot in current column or not we move to n-1 x n-1 matrix so current_row should be increased

    return pivots , Ab

#%%
def backward_elimination(Ab, pivots):
    # we need pivots rows for it then subtract from above rows
    # start from last pivot and keep subtract from above rows
    number_of_pivots = len(pivots)
    pivot_rows = [key[0] for key in pivots.keys()]
    pivot_cols = [key[1] for key in pivots.keys()]
    n_Ab = len(Ab[0])
    for i in range(len(pivot_rows) -1,-1,-1):  #reverse indexing
        #current_col and current_row for pivots
        current_row = pivot_rows[i]
        current_col = pivot_cols[i]

        while current_row > 0:
            # do substraction for all rows above current_row
            factor = Ab[current_row - 1][current_col]
            Ab[current_row - 1] =  [ Ab[current_row - 1][j] - factor * Ab[current_row][j] for j in range(n_Ab) ]


            current_row -= 1

    return Ab
#%%
def switch_two_col(A,c1,c2):
    for i in range(len(A)):
        A[i][c1] , A[i][c2] = A[i][c2], A[i][c1]
#%%
def full_solution(Ab, pivots):
    # check for no solution or not
    m , n = len(Ab), len(Ab[0]) - 1
    d = [ row[-1] for row in Ab ]
    pivot_cols = [key[1] for key in pivots.keys()]
    pivot_rows = [key[0] for key in pivots.keys()]
    print(f"pivot rows are {pivot_rows}")
    print(Ab[pivot_rows[-1] + 1])
    if len(pivot_rows) < m or len(pivot_cols) < n:
        if any(Ab[pivot_rows[-1] + 1]) == False and d[pivot_rows[-1] + 1] != 0:
            print('solutions doesnt exist')
        else:
            print("infinite solutions exits")


    # particular solution vector
    xp = [0] * n
    for i in pivot_rows:
        xp[i] = d[i]
    
    # nullspace columns
    free_cols = [j for j in range(n) if j not in pivot_cols]
    xs = []
    for y in free_cols:
        x = [0] * n
        x[y] = 1
        # now fill pivot variable values from free column -F 
        # but use pivot row because it is pivot row elements that we need value of
        for i, j in enumerate (pivot_cols):
            x[j] = -Ab[pivot_rows[i]][y]

        xs.append(x) 
    return xp, xs
    


#%%
#A = [ [1,3,0,2], [0,0,1,4], [1,3,1,6]] 
A2 = [[1,2,3,5],[0,0,2,2],[0,0,0,0]]
b2 = [0,6,0]
#b = [1,6,7]
print(tabulate(A2, tablefmt='fancy_grid'))
#%%
pivots, R = forward_elimination(A2,b2)
#%%
print(pivots)
print(tabulate(R, tablefmt="fancy_grid"))
#%%
full_rref = backward_elimination(R, pivots)
#%%
print(tabulate(full_rref, tablefmt="fancy_grid"))
#%%
xp, xs= full_solution(full_rref, pivots)
#%%
print(xp, xs)
#%%
 
