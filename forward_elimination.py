def forward_elimination(A, b):
    m, n = len(A) , len(A[0])
    # make augmented matrix [A b]
    Ab = [A[i] + [b[i]] for i in range(m)]
    pivots = {}
    current_row = 0
    for current_col in range(n):
        for row in range(current_row, m):
            pivot = None
            # search all row below untill pivot found 
            if Ab[row][current_col] != 0:
                pivot = Ab[row][current_col]
                pivots[(row, current_col)] = Ab[row][current_col]
                # pivot found swap this row with current row 
                Ab[current_row], Ab[row] = Ab[row], Ab[current_row]

                # normalize this row 
                Ab[current_row] = [x / Ab[current_row][current_col] for x in Ab[current_row]]

                # subtract from below rows
                for i in range(current_row + 1, m):
                    factor = Ab[i][current_col]
                    Ab[i] = [ Ab[i][j] - factor * Ab[current_row][j] for j in range(n + 1) ]

            #if pivot found current_row and current_col increamented
            if pivot != None:
                current_row += 1

    return Ab, pivots

                                                    
if __name__ == '__main__':
    from tabulate import tabulate
    A = [[1,3,0,2],
         [0,0,1,4],
         [1,3,1,6]]
    b = [1,6,7]
    R, pivots = forward_elimination(A,  b)
    print("R is \n")
    print(tabulate(R,tablefmt='fancy_grid'))
    print("pivots are \n", pivots)