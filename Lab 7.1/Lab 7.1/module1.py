import numpy as np

#determinare relatie speciala

def determinareRelatie(multime):
    R = list()
    for a in multime:
        for b in multime:
            if(a < b):
                R.append((a,b))
        
    return R

def reprezentareMatriceala(relatie, n):
    M = np.zeros((n,n))
    M = M.astype(int)

    for elem in relatie:
        a = elem[0]
        b = elem[1]

        M[a-1][b-1] = 1

    return M;

def verificaReflexivitatea(M,n):

    for x in range(0, n):
        if M[0][0]==0:
            return 0

    return 1


def verificaAntiReflexivitatea(M,n):

    for x in range(0, n):
        if M[0][0]==1:
            return 0

    return 1


def verificaSimetria(M):
    Mt = np.matrix.transpose(M)

    #print("M \n", M)
    #print("Mt \n", Mt)

    if np.array_equal(M,Mt):
        return 1

    return 0

def verificaASimetria(M,n):
    Mt = np.matrix.transpose(M)
    Z = np.zeros((n,n))
    I = np.zeros((n,n))

    for x in range(0, n):
        for y in range(0,n):
           if M[x][y] == 1 and Mt[x][y] == 1 :
                I = 1;

    if np.array_equal(I,Z):
        return 1

    return 0

def verificaAntiSimetria(M,n):
    Mt = np.matrix.transpose(M)


    for x in range(0, n):
        for y in range(0,n):
           if M[x][y] == 1 and Mt[x][y] == 1 and ( not M[x][y] )== 1:
                return 0
    return 1

def citireRelatie( multime):
    R = list()
    
    n =int (input('Numarul de legaturi in relatie:\n'))
    i = 0;

    while i < n:
        i = i+1;
        a =int (input('Intert a:\n'))
        b =int ( input('Intert b:\n'))

        if a in multime:
            if b in multime:
                R.append((a,b))

    return R
    