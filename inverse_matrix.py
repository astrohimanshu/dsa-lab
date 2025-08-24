def inverse_matrix(A):
    m,n = len(A), len(A[0])
    if m != n:
        raise ValueError("inverse doesn't exist")

    from forward_elimination import forward_elimination
    from backward_elimination import backward_elimination

    identity = [[1.0 if i == j else 0.0 for j in range(n-1)] for i in range(n)]
    # send augemented [A I] for forward elimination and check pivots
    A_i = [A[i] + identity[i] for i in range(n)]
    b = [0] * n
    b[-1] = 1
    R, pivots = forward_elimination(A_i, b)
    if len(pivots.keys()) < n:
        raise ValueError("Inverse doesn't exits")
    Ro = backward_elimination(R, pivots)
    print(Ro)
    inverse = [[row[j] for j in range(n,2*n) ] for row in Ro ]
    return inverse

if __name__ == '__main__':
    from tabulate import tabulate
    A = [[1,0,0],
         [1,1,0],
         [1,1,1]]
    
    A_inv = inverse_matrix(A)
    print(tabulate(A_inv, tablefmt='fancy_grid'))





