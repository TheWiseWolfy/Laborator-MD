import numpy as np
import module1

    
def main():


    U={1,2,3,4}
    R = module1.citireRelatie( U)
    print("R = ", R)

    n = len(U)
    M = module1.reprezentareMatriceala(R, n)
    print("M \n", M)

    if module1.verificaReflexivitatea(M,n) == 1:
        print("Relatia este reflexiva.")

    if module1.verificaAntiReflexivitatea(M,n) == 1:
        print("Relatia este antireflexiva.")

    if module1.verificaSimetria(M) == 1:
        print("Relatia este simetrica.")

    if module1.verificaASimetria(M,n) == 1:
        print("Relatia este asimetrica.")

    if module1.verificaAntiSimetria(M,n) == 1:
        print("Relatia este antisimetrica.")




main()