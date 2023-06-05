#Para la experiencia 1 se recibe el número de hilos 
#como argumento de entrada y se crea esa
#cantidad de hilos

import sys
from threading import Thread

def greetings(i):

    print(f"Te saluda el thread {i + 1}.")
    

if __name__ == "__main__":

    number_of_threads =int(sys.argv[1])
    threads=[]

    for i in range (number_of_threads):
        
        h= Thread(target=greetings, args=(i, ))
        threads.append(h)
    for h in threads:
        #Inicia el hilo
        h.start()
        #Esperar hasta que el hilo haya terminado
        h.join()

    