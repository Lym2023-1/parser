archivo1= open ("ejemplo.txt")
archivo2= archivo1.read()
archivo= (archivo2.lower())

def generar_palabra (archivo, i):
    str_rta= []
    while (archivo[i] != " ") and (archivo[i]!= ",")and (archivo[i]!= ";")and (archivo[i]!= "[")and (archivo[i]!= "]")and (archivo[i]!= ":")and (archivo[i]!= "|"):
        str_rta.append(archivo[i])
        i+=1
    palabra="".join(str_rta)
    return (palabra, i+1, archivo[i])

def lexer (archivo):
    rta= []
    size= len(archivo)
    j=0
    while j < size:
        palabra, j, siguientepalabra= (generar_palabra(archivo,j))
        rta.append(palabra)
        if siguientepalabra!= " ":
            rta.append(siguientepalabra)
    return rta



def es_palabra_reservada (palabra,lista_palabras_reservadas):
    if palabra in lista_palabras_reservadas:
        return (True)
    else:
        return (False)


#rta= generar_palabra (archivo, 0)
#print (rta)

#a= [palabra.strip() for palabra in archivo.split(" ") if palabra!=""]
print(lexer(archivo))
