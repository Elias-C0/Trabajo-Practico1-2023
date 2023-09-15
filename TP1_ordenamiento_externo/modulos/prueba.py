import heapq

def merge_natural(lista, archivo_salida):
    bloques = []

    # Dividir la lista en bloques iniciales
    with open(archivo_salida, "w") as salida:
        for num in lista:
            salida.write(str(num) + "\n")

    archivo_entrada = archivo_salida
    bloque_actual = []
    bloque_anterior = float('-inf')

    with open(archivo_entrada, "r") as entrada:
        for linea in entrada:
            numero = int(linea.strip())

            if numero < bloque_anterior:
                bloques.append(bloque_actual)
                bloque_actual = []

            bloque_actual.append(numero)
            bloque_anterior = numero

    if bloque_actual:
        bloques.append(bloque_actual)

    while len(bloques) > 1:
        min_heap = [(bloque[0], i, 0) for i, bloque in enumerate(bloques) if bloque]
        heapq.heapify(min_heap)

        lista_ordenada = []

        while min_heap:
            valor, bloque_idx, elemento_idx = heapq.heappop(min_heap)
            lista_ordenada.append(valor)

            if elemento_idx + 1 < len(bloques[bloque_idx]):
                siguiente_valor = bloques[bloque_idx][elemento_idx + 1]
                heapq.heappush(min_heap, (siguiente_valor, bloque_idx, elemento_idx + 1))

        # Escribir los resultados intermedios para la siguiente iteración
        with open(archivo_entrada, "w") as entrada:
            for numero in lista_ordenada:
                entrada.write(str(numero) + "\n")

        bloques = [lista_ordenada]

    # Renombrar el archivo final
    import os
    os.rename(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    archivo_entrada = "datos.txt"  # Reemplaza con el nombre de tu archivo de entrada
    archivo_salida = "archivo_ordenado.txt"  # Nombre del archivo de salida

    with open(archivo_entrada, "r") as arch:
        lista = [int(linea.strip()) for linea in arch]

    merge_natural(lista, archivo_salida)
    print("Archivo ordenado guardado en", archivo_salida)
