
import numpy as np
import time
import matplotlib.pyplot as plt


def alternativa1(M,v):
    
    r=M.dot(v)
    return r
    
    
def alternativa2(M,v):
    r=np.zeros(len(v))
    
    for i in range(len(v)):
        suma=0
        for j in range(len(v)):
            suma = M[i][j] * v[j]  +suma
        r[i] =suma
        
    return r

def alternativa3(M,v):
    r=np.zeros(len(v))
    
    for i in range(len(v)):
        r[i]= M[i].dot(v)
    
    return r

def alternativa4(M,v):
    
    r=np.zeros(len(v))
    i=0
    while (i< len(v)):
        suma=0
        j=0
        while(j<len(v)):
            suma = M[i][j] *v[j] + suma
            j=j+1
        r[i]= suma
        i=i+1
    return r

def alternativa5 (M,v):
    r = np.zeros(len(v))
    for i in range(len(v)):
        suma = 0
        for j in range(len(v)):
            suma = M[i*len(v)+j]*v[j] + suma
        r[i] = suma
        
    return r


if __name__=="__main__":
    
    #Matriz=np.array([[1,2,3], [4,5,6],[7,8,9]])
    #vector=np.array([10,20,30])
    
    #matriz_v= np.reshape(Matriz, [len(vector)*len(vector), 1])
    
    #print(f"Alternativa 1:",alternativa1(Matriz,vector))
    #print(f"Alternativa 2:",alternativa2(Matriz,vector))
    #print(f"Alternativa 3:",alternativa3(Matriz,vector))
    #print(f"Alternativa 4:",alternativa4(Matriz,vector))
    #print(f"Alternativa 5:",alternativa5(matriz_v,vector))
    
    N=1024
    Matriz_vector= np.random.rand(N*N)
    matriz=np.reshape(Matriz_vector, [N,N]) #N filas y N columnas
    vector=np.random.rand(N)
    #LISTAS 
    time_1=[]
    time_2=[]
    time_3=[]
    time_4=[]
    time_5=[]
    iteracion= 100
    
    for _ in range(100):
        t1=time.perf_counter()
        alternativa1(matriz,vector)
        t2=time.perf_counter()
        alternativa2(matriz,vector)
        t3= time.perf_counter()
        alternativa3(matriz,vector)
        t4=time.perf_counter()
        alternativa4(matriz,vector)
        t5=time.perf_counter()
        alternativa5(Matriz_vector,vector)
        t6=time.perf_counter()
        
        time_1.append(t2-t1)
        time_2.append(t3-t2)
        time_3.append(t4-t3)
        time_4.append(t5-t4)
        time_5.append(t6-t5)
    
    plt.show(time_1)
    plt.show(time_1)
    plt.show(time_1)
    plt.show(time_1)
        
    plt.legend(["A1", "A2","A3","A4","A5"])
    
    plt.grid()
    plt.savefig("Matriz_vector.png", dpi=300)
    #COMENTARIOS
    #La alternativa 4 es la más ruidosa y consume mayor tiempo de ejecución (PEOR)
    #La alternativa 3 y 5 son similares en esta escalas y consume menor tiempo de ejecución (MEJOR)