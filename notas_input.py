

import time

def registro_numero(pista:str) -> float:

    num_flag = False
    while not num_flag:
        num=input(pista)
        try: 
            num_val=float(num)
            num_flag=True
        except ValueError:
            pass
    return num_val


if __name__ == '__main__':

    inicio_Total=time.perf_counter()

    labs=list()
    num_labs=14

    tiempo_espera=time.perf_counter()

    for i in range(num_labs):
        lab= registro_numero(f"Por favor, ingrese nota del lab {i+1}: ")
        print(f"Nota recibida: {lab}")
        labs.append(lab)

    Ex1=registro_numero(f"Por favor, ingrese la nota del Exámen 1: ")
    Ex2=registro_numero(f"Por favor, ingrese la nota del Exámen 2: ")

    fin_espera=time.perf_counter()

    tiempo_CPU=time.perf_counter()
    nota_lab=sum(labs)/len(labs)
    nota_final=((5*nota_lab) + (2.5*Ex1) + (2.5*Ex2))/10
    fin_CPU=time.perf_counter()
    
    Fin_total=time.perf_counter()

    print(f"Nota final es: {nota_final}")
    print(f"Tiempo total de ejecución: {Fin_total - inicio_Total} segundos")
    print(f"Tiempo de operaciones E/S: {fin_espera - tiempo_esperacion} segundos")
    print(f"Tiempo de procesamiento: {fin_CPU - tiempo_CPU} segundos")



