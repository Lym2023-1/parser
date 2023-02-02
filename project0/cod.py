archivo= open("ejemplo.txt").read().lower()


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

def generar_palabra (archivo, i):
    generador_palabra= []
    simbolos_cierre={" ",",",",","[","]",":","|"}
    while archivo[i] not in simbolos_cierre:
        generador_palabra.append(archivo[i])
        i+=1
    palabra="".join(generador_palabra)
    return (palabra, i+1, archivo[i])

#Requerimientos

#Crear un diccionario con el nombre de las funciones. La llave es el nombre y el valor la cantidad de parametros
#Crear otro diccionario para las condiciones

""" 
def es_palabra_reservada (palabra,lista_palabras_reservadas):
    if palabra in lista_palabras_reservadas:
        return (True)
    else:
        return (False)

 """
print(lexer(archivo))

