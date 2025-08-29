def full_solutions(Ab, pivots):
    m, n = len(Ab), len(Ab[0]) - 1
    pivot_cols = [ x[1] for x in pivots.keys() ]
    pivot_rows = [ x[0] for x in pivots.keys() ]

    # check if solutions exist or not 

    if len(pivot_rows) < m or len(pivot_cols) < n:
        if any(Ab[pivot_rows[-1] + 1]) == False:
            print('infinite solutions exits')
        else:
            print('No solution exits')
    d = [Ab[i][-1] for i in range(m)]
    # particular solution
    xp = [0] * n
    for i,j in enumerate(pivot_cols):
        xp[j] = d[pivot_rows[i]]

    print(xp)

    # nullspace
    free_cols = [ i for i in range(n) if i not in pivot_cols]
    xs = []
    for i,j in enumerate(free_cols):
        x = [0] * n
        x[j] = 1
        for z,y in enumerate(pivot_cols):
            #if y != j: #pivot column
            x[y] = -Ab[pivot_rows[z]][j]
        xs.append(x)
    return xp, xs

if __name__ == '__main__':
    from forward_elimination import forward_elimination
    from backward_elimination import backward_elimination
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
    xp, xs = full_solutions(R, pivots)
    print('particular solution is :\n')
    print(tabulate([xp], tablefmt='fancy_grid'))
    print('Special solutions are:\n')
    print(tabulate(xs,tablefmt='fancy_grid'))