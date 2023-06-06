

import socket
import numpy as np


#Hallar nota final
def Calcular_promedio(Pa, Pb, Ex1, Ex2):
    nf= (3*Pa) + (3*Pb) + (2*Ex1) + (2*Ex2)
    nf = nf/10
    return nf

if __name__ == '__main__':

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    direccion=("127.0.0.1", 5000)
    servidor.bind(direccion)
    servidor.listen(1) #listen for an incoming connection

    print("El servidor está en espera de una conexión ...")


    while True:

        try:
            conexion, direccion = servidor.accept()

            print(f"Connecting to client at port {conexion}")

            #Recibir la data del cliente 
            datos = conexion.recv(1024).decode()

            Pa, Pb, Ex1, Ex2 = map(float, datos.split(","))

            NF=Calcular_promedio(Pa, Pb, Ex1, Ex2)

            #Retornar la nota final 

            conexion. sendall(str(NF).encode())
        except:
            print("El cliente ha cerrado la conexion.")
        finally:

            conexion.close()
            break



        

        

