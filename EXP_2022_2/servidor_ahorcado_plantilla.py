import random
import socket

my_IP = "127.0.0.1"
port = 5002

#Diccionario de donde se escoge palabras al azar para el juego
dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]

def decifrar_palabra(random_word,hidden_word,client_guess):

    for idx in range(0, len(random_word)):
        if random_word[idx] == client_guess:
            hidden_word = hidden_word[:idx] + client_guess + hidden_word[idx+1:]
    return hidden_word
    
def Esconder_palabra(random_word):
    palabra_oculta=""
    for i in range (len(random_word)):
        palabra_oculta+="*" 
    return palabra_oculta

def client_guess_valido(client_guess, random_word):
     
    for i in range(len(random_word)):
        if client_guess== random_word[i]:
            validacion= True
            break
        else:
            validacion=  False 

    return validacion

if __name__ == "__main__":
	
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Arrancando servidor en {my_IP}")
    cliente_address=(my_IP,port)
    s.bind(cliente_address)
    print(f"Esperando una nueva conexion de un cliente.")
    s.listen(1)
    conn, cliente_address=s.accept()
    print(f"... conexion de: {cliente_address}")

    try:
        msg=conn.recv(1024)
        mensaje_recibido=msg.decode("utf-8")
        if mensaje_recibido=="start":
            print("Recibi el comando start")
            #Elegir una palabra
            random_word=random.choice(dictionary)
            print(f"Palabra elegida: {random_word}")
            #ESconder palabra
            hidden_word=Esconder_palabra(random_word)
            #Enviar palabra oculta selecionada al cliente
            conn.sendall(hidden_word.encode("utf-8"))

            for i in range(0,4):
                #Recibimos la letra elegida
                letra=conn.recv(1024)
                client_guess=letra.decode("utf-8")
                print(f"Client guess: {client_guess}")

                #Si la letra es correcta, desencrita una letra de la palabra 
                if client_guess=="stop":
                    #Se de tiene el juego
                    print("El cliente detuvo el juego. Finalizó la partida.")
                    break
                elif client_guess_valido(client_guess, random_word)==True:
                    hidden_word=decifrar_palabra(random_word,hidden_word,client_guess)
                    if hidden_word == random_word:

                        break
                    else:
                        conn.sendall(hidden_word.encode("utf-8"))
                else:
                    mensaje_error="Intento incorrecto"
                    conn.sendall(mensaje_error.encode("utf-8"))
            print(f"La palabra oculpa era : {random_word}")
        elif mensaje_recibido=="stop":
            print("El cliente detuvo el juego. Finalizó la partida.")
        
        else:
            print("Comando incorrecto. Intentalo de nuevo más tarde.")
  
    finally:
        print("Se terminó la partida.")
        
        conn.close()