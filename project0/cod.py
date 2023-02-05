#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Se lee el archivo y se pasa a minúsculas para evitar inconvenientes"

#archivo= open("ejemplo.txt").read().lower()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ESTRUCTURAS NECESARIAS PARA IDENTIFICAR PALABRAS CLAVE
"""
dic_condicionales= {"facing":"O" , "canput": ("n", "X") , "canpick": ("n", "X") ,
    "canmoveindir": ("n", "D") , "canjumpindir": ("n", "D") ,
    "canmovetothe": ("n", "O") , "canjumptothe": ("n", "O") ,
    "not": None}
"""

dic_condicionales= {"facing":1 , "canput": 2 , "canpick": 2 ,
    "canmoveindir": 2 , "canjumpindir": 2 ,
    "canmovetothe": 2 , "canjumptothe": 2 ,
    "not": None}

dic_comandos= {"assignTo": 1, "goto": 2, "move":1 , "turn":1, "face": 0, "put":2, "pick":2 ,
    "moveindir": 2 , "jumpindir": 2 ,
    "movetothe": 2 , "jumptothe": 2 ,
    "not": None


 }
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#FUNCIONES PARA OBTENER EL LEXER CON SUS TOKENS
"""
El objetivo de la función es generar una palabra del archivo 
de texto, iterando a través de los caracteres en el archivo 
desde la posición i hasta que se encuentra un símbolo de cierre.

El conjunto de símbolos de cierre está definido como 
{" ",",",",","[","]",":","|"} y se utiliza para detener la 
iteración y retornar la palabra generada, el nuevo índice (i+1) y 
el símbolo de cierre encontrado.

La palabra generada es construida a partir de una lista 
generador_palabra que se rellena con los caracteres del archivo, 
y se convierte en una cadena de texto mediante el método join. 
"""

def generar_palabra (archivo, i):
    generador_palabra= []
    simbolos_cierre={" ",",",",","[","]",":","|"}
    while archivo[i] not in simbolos_cierre:
        generador_palabra.append(archivo[i])
        i+=1
    palabra="".join(generador_palabra)
    return (palabra, i+1, archivo[i])

"""
La función lexer toma como entrada un archivo de texto 
y devuelve una lista con las palabras y símbolos encontrados 
en el archivo.

La función utiliza un ciclo while que itera sobre los caracteres
en el archivo hasta que se han procesado todos los caracteres. 
Para cada iteración, la función llama a generar_palabra para generar 
la siguiente palabra y símbolo en el archivo. La palabra y símbolo 
son agregados a la lista rta.

Si el símbolo siguiente a la palabra generada no es un espacio en 
blanco, entonces se agrega a la lista rta.
"""

def lexer (archivo):
    rta= list()
    j=0
    while j < len(archivo):
        palabra, j, siguientepalabra= (generar_palabra(archivo,j))
        rta.append(palabra)
        if siguientepalabra!= " ":
            rta.append(siguientepalabra)
    rta[0]=rta[0].replace("\n","")
    return rta


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#FUNCIONES PARA procesar BLOQUES DE INSTRUCCIONES SEPARADOS"

#revisa de donde a donde estan los procedimientos, retorna si están bien y la posicion final donde terminó de leer
def procesar_todos_procedimientos (lexer: list, posicion_inicial: int):
    return()
#
def procesar_un_procedimiento():
    return()




#Requerimientos

#Crear un diccionario con el nombre de las funciones. La llave es el nombre y el valor la cantidad de parametros
#Crear otro diccionario para las condiciones


def es_palabra_reservada (palabra, dic_condicionales, dic_comandos):
    if palabra in dic_condicionales:
        return (True, (dic_condicionales[palabra]))

    elif palabra in dic_comandos:
        return (True, (dic_comandos[palabra]))
    else: 
        return(False, None)

def funcion_principal(archivo, es_correcto: bool)->bool:
    #FUNCIONAMIENTO GENERAL
    #Esta función itera el lexer paso por paso, usando funciones auxiliares (que a su vez pueden usar más funciones auxiliares, 
    #importante: en vez de una orden simple de avance (i+=1) se utiliza el i que cada función retorna
    #en cada paso, la varialbe "es_correcto" dice si hay o no un error en la syntaxis, si lo hay, se acabará el while, si no, seguirá el while hasta el final de archivo
    #el while pude acabar tanto si variable es correcto es falsa o verdadera, por eso se retorna esta variable, es la respuesta final del programa
    i=0
    longitud= len(lexer) 
    while i<longitud and es_correcto== True:
        palabra_actual=lexer[i]
        es_reservada, palabra= es_palabra_reservada(palabra_actual)
        if es_reservada== True:
            if palabra== "PROCS":
                es_correcto, i= procesar_todos_procedimientos(lexer, [i])

            elif palabra= "VAR":
                es_correcto, i= procesar_todos_vars(lexer[i])

            elif palabra= "VAR":
                es_correcto, i= procesar_todos_vars(lexer[i])
                
            #faltan condiciones, cada condicion debe invocar una funcion que procese una parte del lexer y retorne la posición en la que quedo
            #faltan condiciones
        else: 
            return false

    return es_correcto      

        



    return 


print (funcion_principal(archivo, true))
    
