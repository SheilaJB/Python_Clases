

import socket



if __name__=='__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)

    try:
        s.connect(server_address)
        print("Conectando con el servidor...")
        #Enviar el codigo del alumno

        codigo=str(input())

        s.sendall(codigo.encode())

        #Recibo detalles de la nota 
        datos = s.recv(1024).decode()
        detalle=datos.split(",")

        if len(detalle)>2:
            print(f"Nota de la pregunta 1: {detalle[0]},pregunta 2: {detalle[1]},pregunta 3: {detalle[2]}")
            print(f"Condicion de la nota es {detalle[3]}")
        else:
            print(f"{detalle[0]} {codigo} {detalle[1]}")

    finally:
        print("CErrando conexion con el servidor...")
        s.close()




