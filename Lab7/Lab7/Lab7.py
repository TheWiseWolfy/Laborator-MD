
A = ['a','b','c']
B = ['a','b','d','e']

def reunion(a,b):


    if len(a) > len(b):
         c = a
         for x in a:
             if x not in c:
                  c.append(x)

    if len(a) < len(b):
        c = b
        for x in a:
            if x not in c:
                c.append(x)


    return c;

def intersection(a,b):
    if len(a) > len(b):
        a, b = b, a

    c = []
    for x in a:
        if x in b:
            c.append(x)
    return c

def diference(a,b):

    c = []
    for x in a:
        if x not in b:
            c.append(x)
    return c


def diferenceSim(a,b):

    c = []
    D1 =diference(A,B)
    D2 =diference(B,A)
    U =reunion(D1, D2 )

    return U

def main(): 
 
    U =reunion(A,B)
    I =intersection(A,B)
    D1 =diference(A,B)
    D2 =diference(B,A)
    DS =diferenceSim(A,B)


    print("A             B               AUB         AIB           A/B           B/A           ASB" ,end = '')
    for x in U:
       
        print("\nPentru %s:  "% x)

        if x in A:
            print( "True          ", end = '')
        if x not in A:
            print( "False         ", end = '')

        if x in B:
            print( "True          ", end = '')
        if x not in B:
            print( "False         ", end = '')

        if x in U:
            print( "True          ", end = '')
        if x not in U:
            print( "False         ", end = '')

        if x in I:
            print( "True          ", end = '')
        if x not in I:
            print( "False         ", end = '')

        if x in D1:
            print( "True          ", end = '')
        if x not in D1:
            print( "False         ", end = '')

        if x in D2:
            print( "True          ", end = '')
        if x not in D2:
            print( "False         ", end = '')


        if x in DS:
            print( "True          ", end = '')
        if x not in DS:
            print( "False         ", end = '')


main()