#Euler

import numpy as np 


def euler(x):
    return pow(1+1/x,x)
    
if __name__=="__main__":
    N=1000
    lista_numero=np.zeros(N)
    
    
    for x in range(1,N):
        lista_numero=euler(x)
        
    print(lista_numero)

    
    