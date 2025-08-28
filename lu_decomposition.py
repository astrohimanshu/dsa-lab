def lu_decomposition(A):
    # get rows and columns of A
    m, n = len(A), len(A[0])
    # set permutation vector p
    p = [ i + 1 for i in range(m) ]
    current_row = 0
    pivots = {}
    # declare m by m L matrix
    L = []

    for i in range(m):
        L.append([0]*m)
        L[i] = [1 if i == j else 0 for j in range(m)]
        
    for current_col in range(n):
        pivot = None

        for row in range(current_row, m):
            if A[row][current_col] != 0:
                pivot = A[row][current_col]
                pivots[(row,current_col)] = pivot

                # swap if row != current_row also swap permutation vector
                A[row][current_col], A[current_row][current_col] = A[current_row][current_col], A[row][current_row]
                p[row], p[current_row] = p[current_row], p[row]

                # do elimination on rows below current row
                for i in range(current_row + 1, m):
                    factor = A[i][current_col] / pivot
                    A[i] = [ A[i][j] - A[current_row][j] * factor for j in range(n) ]
                    L[i][current_col] = factor

               # after elimination move on to next row and col
                break
        if pivot != None:
            current_row += 1
        
    # make permutation matrix from P ( m by m )
    P = []
    for row in range(m):
        P.append([0] * m)
        print(P)
        P[row][p[row] - 1] = 1
        
    return L, A, P

if __name__ == '__main__':
    from tabulate import tabulate
    A = [[1,2,3],
         [1,2,3]]
    L, U, P  = lu_decomposition(A)

    print(tabulate(U, tablefmt = 'fancy_grid'))
    print(tabulate(L, tablefmt = 'fancy_grid'))
    print(tabulate(P, tablefmt = 'fancy_grid'))
