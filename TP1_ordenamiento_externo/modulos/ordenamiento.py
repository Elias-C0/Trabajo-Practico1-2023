import os
import time

def mezcla_directa(archivo_in,B:int):
  #Se leen los datos de entrada y se almacenan en una lista
  lista=[]
  with open(archivo_in, "r") as arch:
    for linea in arch:
      lista.append(int(linea)) #.strip()
  
  #Dividimos la lista en bloques, los ordenamos y escribimos archivos temporales
  contador= 1
  for x in range(0,len(lista),B):
    bloque= lista[x:x + B]
    bloque.sort()
    with open(f"bloque_temporal_{contador}.txt", "w") as temporal:
      for dato in bloque:
        temporal.write(f"{dato}\n")
    contador +=1

  lista_ordenada= ord_bloques([f"bloque_temporal_{numero}.txt" for numero in range(1,contador)]) #llamamos a una funcion para que funione los bloques en solo archivo

  #Escribirmos la lista ordenada en un archivo nuevo
  with open("Archivo_ordenado.txt", "w") as salida:
    for x in lista_ordenada:
      salida.write(f"{x}\n")

  for i in range(1,contador):
    os.remove(f"bloque_temporal_{i}.txt") #Eliminamos los archivos temporales
  

def ord_bloques(bloques):
    archivos_bloques = [open(bloque, "r") for bloque in bloques] #Abrimos los archivos de bloques

    lista_ordenada = []

    valores_bloques = [archivo.readline().strip() for archivo in archivos_bloques]

    while any(valores_bloques):
        
        valores_validos = []
        for valor in valores_bloques:
           if valor.isdigit():    # Se verifican que los valores sean digitos
              valores_validos.append(valor)

        if not valores_validos: #En caso de los bloques esten vacios se sale del bucle.
            break

        valor_minimo = min(valores_validos)
        lista_ordenada.append(valor_minimo)

        min_indice = valores_bloques.index(valor_minimo) #Se busca el índice del bloque del que proviene el mínimo

        nuevo_valor = archivos_bloques[min_indice].readline().strip() #Lee el siguiente valor del bloque del cual se extrajo el minimo

        valores_bloques[min_indice] = nuevo_valor

    for archivo in archivos_bloques: #Cerramos los archivos de bloques
        archivo.close()

    return lista_ordenada #Retornamos la lista ordenada


def verificaciones(archivo_original:str,archivo_ordenado:str):
  lista=[]
  with open(archivo_original, "r") as arch:
    for linea in arch:
      lista.append(int(linea))
  
  lista_ordenada = []
  with open(archivo_ordenado, "r") as arch2:
    for linea in arch2:
      lista_ordenada.append(int(linea))

  # Obtenemos el tamaño en bytes de ambos archivos.
  tamano_original= os.path.getsize(archivo_original)
  tamano_ordenado= os.path.getsize(archivo_ordenado)
  tamano_concide= False
  if tamano_original == tamano_ordenado:
     tamano_concide = True
  
  return lista_ordenada == sorted(lista), tamano_concide

#----------------------------------------------------------------------------------------
archivo_in = "datos.txt"
archivo_ordenado= "Archivo_ordenado.txt"
B = 1000000 # Tamaño del bloque

#Muestro el tiempo que tarda en ejecutarse el algoritmo
tic= time.time()# Registro el tiempo de inicio
mezcla_directa(archivo_in, B)
toc= time.time()

tiempo_ejecucion= toc - tic #Se restan los valores para obtener el tiempo de ejecucion
print("Tiempo de ejecución:", round(tiempo_ejecucion,3), "segundos")

verificacion, tamano_coincide= verificaciones(archivo_in,archivo_ordenado)

if verificacion:
   print("Los datos estan ordenados correctamente.")
if tamano_coincide:
   print("El tamaño de los archivos coincide")
else:
   print("El ordenamiento falló")