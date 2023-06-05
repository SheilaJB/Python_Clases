

if __name__ == '__main__':

    with open("READAME.md", "r") as f:
        contenido= f.read()
    filas=contenido.split.split("\n")
    
    notas=list()
    for i in range(1, len(filas)):
        fila=filas[i]

        valores=fila.split(",")
        num=list()
        for valor in valores:
            num.append(float(valor))
            notas.append(nums)

            print(notas)
    

    #----------------------------------------------------------------
    #contenido="esta es la primera linea\n esta es la segunda linea"
    #lineas=contenido.split("\n")

    #contenido= f"{lineas[0].upper()}\n{lineas[1]}"
    #print(contenido)

    #---------------------------------------------------------------
    #my_str="este es un 11 str, HOLA"
    #my_str.split("")->Separa un string en varios strings
    #my_str.upper()-> Convierte todo el string en mayúscula 
    #my_str.lower() -> Convierte todo el string en minúscula
    #my_str.isupper() ->Verifica si toda el string esta en mayúscula
    #my_str.islower() ->Verifica si toda el string esta en minúscula
    #my_str[0] ->Muestrea el primer str de la cadena
    #my_str[0:4] ->Muestra 'este', siempre es +1 de la cantidad que deseamos mostrar

