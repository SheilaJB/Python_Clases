

import socket
import numpy as np

SOCK_BUFFER = 1024

if __name__=='__main__':
    
    #Reading data from 'notas.csc'
    with open("notas.csv", "r") as f:
        contenido = f.read()

    #Si el contenido contiene varias filas de las notas de los estudiantes, entonces 
    # primero separamos las filas       
    filas =contenido.split("\n")

    #Ahora obtenemos las notas de cada fila en una lista
    notas=[]
    for i in range (1, len(filas)):
        fila=filas[i]
        valores = fila.split(",") #lista de las notas sin ,
        notas.append(valores)
        #numeros=list()  

        #for valor in valores:
         #   numeros.append(float(valor))

    #lista que contiene las notas

    #Conectar con un servidor para obtener el promedio final
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("127.0.0.1", 5000)

    s.connect(server_address)

    print(f"Conexion with server address ...")


    #Son 4 notas de prácticas
    practica= notas[0: 4]
    #Se elimina la menor nota 
    practica.remove(min(practica))
    #Sacar promedio de las notas de las practicas
    Pa= np.mean(practica)

    #son 5 notas de laboratorio
    Laboratorio=notas[4: 9]
    #sacar promedio de las notas del laboratorio
    Pb= mean(Laboratorio)

    #notas de los examenes
    Examen1=notas[9]
    Examen2=notas[10]

    data = f'{Pa}, {Pb} ,{Examen1}, {Examen2}'
    try: 
        #Enviando las notas
        s.sendall(data.encode())
        #REcibir promedio final
        promedio_final=s.recv(1024).decode()
        print(f"El promedio final es {promedio_final}")
        
    finally: 
        print("Cerrando conexion.")
        s.close()
