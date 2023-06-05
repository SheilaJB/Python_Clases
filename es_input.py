
import time

if __name__ == '__main__':

    tiempo_registro=list()
    inicio=time.perf_counter()


    #recepcion de data (Operacion E/S)
    num_flag=False
    
    while not num_flag:
        inicio_registro=time.perf_counter()
        num=input("Ingrese un numero: ")
        fin_registro=time.perf_counter()

        tiempo_registro.append(fin_registro-inicio_registro)

        try: 
            num_val=float(num)

            num_flag=True

        except ValueError:
            pass

    #Procedimiento
    resultado= num_val**2
    
    final=time.perf_counter()

    #Operacion de salida
    print(f"El valor ingresado es {num_val} y el resultado al cuadrado es {resultado}")
    print(f"El tiempo total de ejecucion fue {final-inicio} segundos")





    


#-------------------------------------------------------------
    #dato_bytes=dato.encode("utf-8")
    #print(dato.upper())
    #print(type(dato_bytes))
#-------------------------------------------------------------
    #str_chain= "esta es una ñ"
    #print((str_chain))
    #str_bytes= str_chain.encode("utf-8")
    #print((str_bytes))
    #str_bytes1=b'esta es una \xc3\xb1'
    #print((str_bytes1))
    #str_chain1= str_bytes1.decode("ascii")






