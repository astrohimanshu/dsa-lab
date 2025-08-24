def backward_elimination(Ab, pivots):
    m, n = len(Ab) , len(Ab[0]) - 1
    pivot_row_idx = [x[0] for x in pivots.keys()]
    pivot_col_idx = [x[1] for x in pivots.keys()]

    row = len(pivot_col_idx) - 1 
    while row > 0 :
      
        current_pivot_col, current_pivot_row = pivot_col_idx[row], pivot_row_idx[row]

        for i in range(current_pivot_row - 1,-1,-1):
            # subtract all row above by multiplying current row with factor of above row along the pivot col

            factor = Ab[i][current_pivot_col]
            Ab[i] = [Ab[i][j] - factor * Ab[current_pivot_row][j] for j in range(n + 1) ]

        row = row - 1

    return Ab


if __name__ == '__main__':

    from forward_elimination import forward_elimination
    from tabulate import tabulate

    A = [[1,2,1,0],
        [2,4,4,8],
        [4,8,6,8]]
    
    b = [4,2,10]

    R, pivots = forward_elimination(A,  b)
    print("R is \n")
    print(tabulate(R,tablefmt='fancy_grid'))
    print("pivots are \n", pivots)

    Ro = backward_elimination(R, pivots)
    print("Ro is \n")
    print(tabulate(Ro, tablefmt="fancy_grid"))