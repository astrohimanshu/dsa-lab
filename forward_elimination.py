def forward_elimination(A: list[list], b: list) -> 'list[list[float]], dict[tuple[int, int], float]':
    
    m, n = len(A) , len(A[0])
    # make augmented matrix [A b]
    Ab = [A[i] + [b[i]] for i in range(m)]
    pivots = {}
    current_row = 0
    for current_col in range(n):
        pivot = None
        for row in range(current_row, m):
            #pivot = None
            # search all row below untill pivot found 
            if Ab[row][current_col] != 0:

                pivot = Ab[row][current_col]
                
                # pivot found swap this row with current row 
                Ab[current_row], Ab[row] = Ab[row], Ab[current_row]

                # save pivot positions
                pivots[(row, current_col)] = Ab[row][current_col]

                # normalize this row 
                Ab[current_row] = [x / Ab[current_row][current_col] for x in Ab[current_row]]

                # elimination of rows below current row
                for i in range(current_row + 1, m):
                    factor = Ab[i][current_col]
                    Ab[i] = [ Ab[i][j] - factor * Ab[current_row][j] for j in range(n + 1) ]
                    
                # avoid multiple processing of same column
                break

        #if pivot found, current_row and current_col increamented,
        # if pivot is not found only increment column as pivot could be in next column if first col is all zero
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