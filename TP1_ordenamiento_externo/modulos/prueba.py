import heapq
import os
import time

def mezcla_natural(archivo_in, archivo_out, B):
    # Leer el archivo en bloques de tamaño B
    with open(archivo_in, 'r') as input:
        lineas = input.readlines()

    num_bloques = len(lineas) // B + (1 if len(lineas) % B != 0 else 0)

    # Ordenar cada bloque y escribirlo a un archivo temporal
    for i in range(num_bloques):
        bloque = lineas[i * B:(i + 1) * B]
        bloque.sort()

        with open(f'tmp_bloque_{i}.txt', 'w') as tmp_file:
            tmp_file.writelines(bloque)

    # Fusionar los bloques ordenados
    bloques = [open(f'tmp_bloque_{i}.txt', 'r') for i in range(num_bloques)]
    with open(archivo_out, 'w') as output:
        merge_bloques(bloques, output)

    # Cerrar y eliminar archivos temporales
    for i in range(num_bloques):
        bloques[i].close()
        os.remove(f'tmp_bloque_{i}.txt')

def merge_bloques(bloques, output):
    heap = []

    # Inicializar el montículo con el primer elemento de cada bloque
    for i, bloque in enumerate(bloques):
        line = bloque.readline()
        if line:
            heapq.heappush(heap, (int(line), i))

    # Fusionar bloques hasta que el montículo esté vacío
    while heap:
        val, bloque_idx = heapq.heappop(heap)
        output.write(f"{val}\n")

        next_line = bloques[bloque_idx].readline()
        if next_line:
            heapq.heappush(heap, (int(next_line), bloque_idx))

if __name__ == "__main__":
    archivo_in = "datos.txt"  # Reemplaza con el nombre de tu archivo de entrada
    archivo_out = "archivo_ordenado.txt"  # Nombre del archivo de salida
    B = 1000000  # Tamaño del bloque

    time_start = time.time()  # Registra el tiempo de inicio
    mezcla_natural(archivo_in, archivo_out, B)
    time_end = time.time()  # Registra el tiempo de finalización

    tiempo_ejec = time_end - time_start  # Calcula el tiempo de ejecución en segundos
    print("Tiempo de ejecución:", round(tiempo_ejec,3), "segundos")
    print("Archivo ordenado guardado en", archivo_out) 
    #hay que cambiar varias cosas,diosnosampare