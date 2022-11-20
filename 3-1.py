def solution(m):
    
    """
    To solve this problem, consider absorbing Markov chains.
    We need to use fundamental matrix:
        S = (I - B)^-1
    Where I is identity matrix and B is input matrix, changed to fractions.
    
    """
    
    from fractions import Fraction as F

    def fractions(Matrix):
        """
        Changes int probability to decimal fraction
        :param Matrix: initial list of lists
        :returns: list of lists, each cell divided by sum of row
        """
        Fraction_matrix = []
        for row in Matrix:
            S = sum(row)
            if S != 0:
                fraction_row = [F(x,S) for x in row]
                #fraction_row = [(float(x)/float(S)) for x in row]
                Fraction_matrix.append(fraction_row)
            else:
                fraction_row = [0 for x in row]
                Fraction_matrix.append(fraction_row)
        return Fraction_matrix

    def sub_mx(mxA,mxB):
    #For purpose of this exercise I assume mxA has the same size as mxB    
        L = len(mxA)
        C =  [[mxA[i][j]-mxB[i][j] for j in range(L)] for i in range(L)]
        return C

    def copy_matrix(matrix):
        """
        Creates copy of a matrix
        :param matrix: list of lists, matrix to be copied.
        :returns copy: list of lists, duplicate of a matrix.
        """
        rows = len(matrix)
        copy = [[0 for j in range(L)] for i in range(L)]

        for i in range(rows):
            for j in range(rows):
                copy[i][j] = matrix[i][j]
        return copy

    def inverse_matrix(M):
        """
        I use Gauss elimination for matrix inversion.
        Function works on a COPY of original matrix.
        :param M: Transition matrix,
        :param I: Identity matrix,
        :returns Sc: for testing purposes only - should be diagonal.
        :returns Ic: Inversed matrix 
        """
        L = len(M)
        Sc = copy_matrix(M)
        Ic = [[F(1) if j==i else F(0) for j in range(L)] for i in range(L)]

        for i in range(L):
            for j in range(L):
                if i != j:
                    norm = Sc[i][i]
                    #Normalize each row to 1
                    Sc[i] = [x/norm for x in Sc[i]]
                    Ic[i] = [x/norm for x in Ic[i]]
                    #Substract to create diagonal matrix
                    if Sc[j][i] != 0:
                        scale = Sc[i][i]/Sc[j][i]
                        Sc[j] = [Sc[j][k]-Sc[i][k]/scale for k in range(L)]
                        Ic[j] = [Ic[j][k]-Ic[i][k]/scale for k in range(L)]
        return(Ic,Sc)

    def terminal_states(matrix):
        """
        Checks which states are terminal
        """
        Is_terminal = [False for x in matrix ]
        for n in range(0,len(matrix)):
            if (all(x==0 for x in matrix[n])) or (sum(matrix[n])==1 and matrix[n][n]==1):
                Is_terminal[n] = True
        return(Is_terminal)
    
    
    def lcm(a, b):
        """
        Determine the largest common denominator
        """
        i = 1
        if a > b:
                c = a
                d = b
        else:
                c = b
                d = a
        while True:
                if (float(c * i) / float(d)).is_integer():
                        return c * i
                i += 1;
    
    #======================Solution======================#
    L = len(m)
    B = fractions(m)
    T = terminal_states(m)

    #Identity matrix
    I = [[F(1) if j==i else F(0) for j in range(L)] for i in range(L)]
    S = sub_mx(I,B)
    inv, diag = inverse_matrix(S)

    #Write probabilities
    P = [inv[0][i] for i in range(len(T)) if T[i]==True]
    
    final = []
    d = 1
    #Calculate common denominator
    for i in P:
        if i.numerator != 0:
            d = lcm(d,i.denominator)
    #Write results
    for i in P:
        if i.numerator == 0:
            final.append(0)
        else:
            x =d/i.denominator
            final.append(int(i.numerator*x))
    final.append(d)
            
    return(final)