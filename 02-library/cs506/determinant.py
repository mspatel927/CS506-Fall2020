# Finds and returns the determinant of an n x n matrix (input as a 2-D list) recursively 

def determinant(A):
    if len(A) != len(A[0]) or len(A) < 2:
        raise ValueError("not a square matrix!")
    else:
        if len(A) == 2:
            det = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
            return det
        else:
            det = 0 
            for j in range(0,len(A)):
                partial = (-1)**(1+j+1)
                partial *= A[0][j]
                A_1j = []
                if j == 0:
                    A_1j = [x[1:] for x in A[1:]]
                else:
                    A_1j = [x[0:j] + x[j+1:] for x in A[1:]]
                print(A_1j)
                partial *= determinant(A_1j)
                det += partial
            return det

