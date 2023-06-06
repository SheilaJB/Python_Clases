
#Servidor

import socket

#Validar código:
def Validar_codigo(codigo_alumno,Codigos_PUCP):

    for codigo in Codigos_PUCP:
        if codigo_alumno==codigo:
            return True
        else: 
            return False


#Hallar condicion de nota final
def Hallar_condicion_nota(NF):
    
    if NF >=10.5:
        condicion="Aprobado"
    else: 
        condicion="No aprobado"

    return condicion
        
  #Detalles de la nota
def Obtener_detalles_nota(codigo_alumno, lista_notas,Codigos_PUCP):
    n=0
    for codigo in Codigos_PUCP:
        if codigo_alumno==codigo:
            n+=1
        
    notas=int(3*n)

    p3=lista_notas[notas-1]
    p2=lista_notas[notas-2]
    p1=lista_notas[notas-3]

    NF=float(p1+p2+p3)

    return p1,p2,p3,NF


if __name__=="__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_addr = ("0.0.0.0", 5000)

    s.bind(server_addr)

    #Lee las notas 
    with open("notas.csv", "r") as f:
        contenido = f.read()

    filas= contenido.split("\n")

    notas_alumno=[]
    lista_codigos=[]
    
    for i in range(1, len(filas)):
        fila=filas[i]
        valores=fila.split(",")

        for n in range(len(valores)):
            if n==0:
                lista_codigos.append(valores[0])
            else:
                notas_alumno.append(valores[1:])
    lista_notas=notas_alumno
    Codigos_PUCP=lista_codigos

    s.listen(1)
    while True:
        try:
            print("Esperando conexiones...")
            conn, client_address = s.accept()

            print(f"Conexion desde {client_address[0]}: {client_address[1]}...")

            #Recibir el codigo del alumno
            print(f"Ingrese su código PUCP: ")

            codigo_alumno=str(conn.recv(1024).decode("utf-8")) #se obtiene una cadena

            if Validar_codigo(codigo_alumno,Codigos_PUCP) == True:
                #enviar detalles de la nota(p1,p2,p3) y la condicion de aprobado
                
                p1,p2,p3,NF= Obtener_detalles_nota(codigo_alumno, lista_notas,Codigos_PUCP)
                condicion=Hallar_condicion_nota(NF)
                data = f'{p1}, {p2} ,{p3}, {condicion}'
                conn.sendall(data.encode())

            else:  
                #Codigo no figura en la lista de alumnos del curso
                data = f'{"El alumno"}, {"no está inscrito en 1IEE06"}'
                conn.sendall(data.encode())
                print(f"El alumno {codigo_alumno} no está inscrito en 1IEE06")

        except ConnectionRefusedError():
            print("Error de conexion al cliente.")
        finally:
            conn.close()
            pass