from TP1_LDE_testing.Modulos.listadoble import ListaDobleEnlazada
import matplotlib.pyplot as plt
import numpy as np
import time

def grafico(numero): #Se utiliza para comprobar el rendimiento de ordenamiento de esta lista doblemente enlazada
  tamano = np.logspace(1, numero, 50)
  tiempos = []
  for cant in tamano:
    tiempo_inicial = time.time()
    total = 0
    for i in range(int(cant)):
      for j in range(int(cant)):
        total += 1
    tiempo_final = time.time()
    duracion_total = tiempo_final - tiempo_inicial
    tiempos.append(duracion_total)

  plt.plot(tamano, tiempos, ".")
  plt.xlabel("Tamaño de la lista")
  plt.ylabel("Tiempo de ejecución (segundos)")
  plt.title("Análisis de Rendimiento")
  plt.grid(True)
  plt.show()

aux = ListaDobleEnlazada()

grafico(4)