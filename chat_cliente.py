import socket 
#CLIENTE PUERTO: 5000

if __name__ == "__main__":


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_address=('0.0.0.0', 5000)
    s.connect(server_address)

    try:
        banderal= True
        while bandera == True:
            #Recibir mensaje del server
            msg_recibido=s.recv(1024)
            #Mensaje de confirmacion
            confirmacion=msg_recibido.decode("utf-8")

            if confirmacion == "salir":
                #Termina la conversacion
                bandera = False

            else:
                #Continuar conversacion
                print("Recibí: " + confirmacion)
                msg=input()
                s.send(msg.encode("utf-8"))
    finally:
        s.close()