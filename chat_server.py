
import socket 
#server PUERTO: 5000

if __name__ == "__main__":


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serve_address=('0.0.0.0', 5000)
    print("Server started and listening on port 5000")

    s.bind(serve_address)
    s.listen(1)
    
    conn, cliente_address = s.accept()
    print("Conectado a cliente: ('127.0.0.1:5000')")

        

    try: 
        bandera = True
        while bandera==True:

            #Conectar al cliente por mesnaje
            msg=input()
            #Se envia este mensaje al cliente para iniciar la conversacion
            conn.sendall(msg.encode("utf-8"))
            #Recibo mensaje de confirmacion del cliente
            confirmacion=conn.recv(1024).decode("utf-8")
            if confirmacion=="salir":
                #Termina la conversacion con el cliente
                bandera=False
            else:
                print("Recibido: " + confirmacion)
    except:
        print("La conversación terminó.")
    finally:
        print("...")
        conn.close()