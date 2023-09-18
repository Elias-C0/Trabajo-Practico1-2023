from TP1_LDE_testing.Modulos.listadoble import ListaDobleEnlazada
from random import shuffle

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
palos = ['♠', '♥', '♦', '♣']

class Carta:
  def __init__(self,valores,palos):
    self.valores = valores
    self.palos = palos

  def __str__(self):
    return f"{self.valores}{self.palos}" #Es para mostrar el valor de las cartas
  
class Mazo:
  def __init__(self):
    self.mazo= ListaDobleEnlazada() #se usa la lista doblemente enlazada para el mazo

  def generar_mazo(self):
    for palo in palos: #Se le agregan las cartas con los valores y palos al mazo
      for valor in valores:
          self.mazo.agregar_al_final(Carta(valor,palo))

  def barajar(self):
    self.generar_mazo()
    cartas_lista = list(self.mazo)
    shuffle(cartas_lista) #mezclamos las cartas
    self.mazo = ListaDobleEnlazada()
    for carta in cartas_lista:
      self.mazo.agregar_al_final(carta) #😆

  def repartir(self):
    jugador_1 = Mazo() #Se le asignan a los jugadores los metodos de Mazo
    jugador_2 = Mazo()
    for x,carta in enumerate(self.mazo): #Se itera sobre el mazo y se reparten las cartas para cada jugador
      if x % 2 == 0:
        jugador_1.poner_arriba(carta)
      else:
        jugador_2.poner_arriba(carta)
    return jugador_1, jugador_2

  def poner_arriba(self, carta):
    self.mazo.agregar_al_inicio(carta)

  def poner_abajo(self, carta):
    self.mazo.agregar_al_final(carta)

  def sacar_arriba(self, jugador=None):
    if not self.mazo.esta_vacia():
        return self.mazo.extraer(0)
    else:
        otro_jugador = 1 if jugador == 2 else 2
        self.ganador = otro_jugador
        print(f"El jugador {jugador} se quedó sin cartas para continuar con el juego")
        print(f"\n                               ***** Jugador {otro_jugador} gana la partida *****")
        exit(1) #si un jugador no tiene cartas para jugar, se termina el juego
  
  def __iter__(self):
    return iter(self.mazo)

class JuegoDeGuerra:
  def __init__(self, limite_turnos=10000):
    self.turno = 1
    self.max_turnos = limite_turnos
    self.ganador = None

  def imprimir_mazo(self, jugador): #imprime el mazo de cada jugador
    for x in range(len(jugador.mazo)):
      print("-X ", end=" ") 
      if (x + 1) % 10 == 0:
        print()
    print()

  def imprimir_botin_guerra(self,botin): #imprime el botin en juego segun cuantas guerras seguidas se produjeron
    lista_botin= list(botin)
    if len(lista_botin) == 10:
      print()
      print(f"         {lista_botin[0]} {lista_botin[1]}", end=" ")
      print("-X " * 6, end="")
      print(f"{lista_botin[8]} {lista_botin[9]}")
      print("\n")
    elif len(lista_botin) == 18:
      print()
      print(f"         {lista_botin[0]} {lista_botin[1]}", end=" ")
      print("-X " * 6, end="")
      print(f"{lista_botin[8]} {lista_botin[9]}")
      print("-X " * 6, end="")
      print(f"{lista_botin[16]} {lista_botin[17]}")
      print("\n")
    elif len(lista_botin) == 26:
      print()
      print(f"         {lista_botin[0]} {lista_botin[1]}", end=" ")
      print("-X " * 6, end="")
      print(f"{lista_botin[8]} {lista_botin[9]}")
      print("-X " * 6, end="")
      print(f"{lista_botin[16]} {lista_botin[17]}")
      print("-X " * 6, end="")
      print(f"{lista_botin[24]} {lista_botin[25]}")
      print("\n")
    elif len(lista_botin) == 34:
      print()
      print(f"         {lista_botin[0]} {lista_botin[1]}", end=" ")
      print("-X " * 6, end="")
      print(f"{lista_botin[8]} {lista_botin[9]}")
      print("-X " * 6, end="")
      print(f"{lista_botin[16]} {lista_botin[17]}")
      print("-X " * 6, end="")
      print(f"{lista_botin[24]} {lista_botin[25]}")
      print("-X " * 6, end="")
      print(f"{lista_botin[32]} {lista_botin[33]}")
      print("\n")

  def jugar_ronda(self):
    carta_jugador_1 = self.jugador_1.sacar_arriba(1) #se extraen las cartas de arriba del mazo de cada jugador
    carta_jugador_2 = self.jugador_2.sacar_arriba(2)

    if carta_jugador_1 is None or carta_jugador_2 is None: #comprobacion de que si algun jugador se quedo sin cartas en su mazo
      if len(self.jugador_1.mazo) > len(self.jugador_2.mazo):
        self.ganador = "Jugador 1"
      elif len(self.jugador_2.mazo) > len(self.jugador_1.mazo):
        self.ganador= "Jugador 2"

    #lineas que imprime en la consola segun el estado actual del juego
    print("\n-------------------------------------")
    print(f"Turno: {self.turno}")
    print("Jugador 1:")
    self.imprimir_mazo(self.jugador_1)
    print()
    print(f"         {carta_jugador_1} {carta_jugador_2}\n")
    print("Jugador 2:")
    self.imprimir_mazo(self.jugador_2)

    valor_carta_jugador_1 = valores.index(carta_jugador_1.valores) + 2
    valor_carta_jugador_2 = valores.index(carta_jugador_2.valores) + 2

    if valor_carta_jugador_1 > valor_carta_jugador_2:
      self.jugador_1.poner_abajo(carta_jugador_1)
      self.jugador_1.poner_abajo(carta_jugador_2)

    elif valor_carta_jugador_1 < valor_carta_jugador_2:
      self.jugador_2.poner_abajo(carta_jugador_1)
      self.jugador_2.poner_abajo(carta_jugador_2)

    else:
      print("\n-------------------------------------")
      print(" " *25, "**** Guerra!! ****")
      self.jugador_1.poner_arriba(carta_jugador_1)
      self.jugador_2.poner_arriba(carta_jugador_2)
      self.guerra()

    self.turno += 1
  
  def guerra(self):
    self.turno +=1
    botin=Mazo()
    
    #comprobacion de que si algun jugador no tiene las suficientes cartas para jugar la guerra
    if len(self.jugador_1.mazo) < 4 or len(self.jugador_2.mazo) < 4:
      if len(self.jugador_1.mazo) < 4:
        self.ganador = "Jugador 2"
        print("El Jugador 1 no tiene suficientes cartas para continuar la guerra")
      elif len(self.jugador_2.mazo) < 4:
        self.ganador = "Jugador 1"
        print("El Jugador 2 no tiene suficientes cartas para continuar la guerra")
      else:
        self.turno = self.max_turnos + 1

    carta_jugador_1 = self.jugador_1.sacar_arriba(1) #extrae las cartas que dieron como resultado guerra
    carta_jugador_2 = self.jugador_2.sacar_arriba(2)
    botin.poner_abajo(carta_jugador_1) #las guarda en un botin
    botin.poner_abajo(carta_jugador_2)

    hay_guerra= True 
    while hay_guerra: #para cada vez que este en True, sigue jugandose una guerra
      for h in range(3): #saca 3 cartas de cada jugador y las guarda en botin
        carta1 = self.jugador_1.sacar_arriba(1)
        carta2 = self.jugador_2.sacar_arriba(2)

        if carta1 is not None:
          botin.poner_abajo(carta1)
        else:
          self.ganador = "Jugador 2"
          hay_guerra= False
          self.turno = self.max_turnos + 1 # sirve para finalizar la partida cuando, en este caso, el jugador 1 no cuenta con mas cartas

        if carta2 is not None:
          botin.poner_abajo(carta2)
        else:
          self.ganador = "Jugador 1"
          hay_guerra= False
          self.turno = self.max_turnos + 1

      carta_jugador_guerra_1 = self.jugador_1.sacar_arriba(1) #las nuevas cartas que se comparan
      carta_jugador_guerra_2 = self.jugador_2.sacar_arriba(2)
      botin.poner_abajo(carta_jugador_guerra_1)
      botin.poner_abajo(carta_jugador_guerra_2)

      print(f"Turno: {self.turno}")
      print("Jugador 1:")
      self.imprimir_mazo(self.jugador_1)
      self.imprimir_botin_guerra(botin) #imprime el botin en juego (las cartas que se llevara el ganador)
      print("Jugador 2:")
      self.imprimir_mazo(self.jugador_2)

      valor_carta_guerra_1 = valores.index(carta_jugador_guerra_1.valores) + 2
      valor_carta_guerra_2 = valores.index(carta_jugador_guerra_2.valores) + 2

      if valor_carta_guerra_1 > valor_carta_guerra_2:
        for x in botin:
          self.jugador_1.poner_abajo(x) #guarda todo el botin en el ganador en el orden correspondiete
        hay_guerra= False #cambia el estado para que salga del bucle

      elif valor_carta_guerra_1 < valor_carta_guerra_2:
        for x in botin:
          self.jugador_2.poner_abajo(x)
        hay_guerra= False

      else:
        print("\n-------------------------------------")
        print(" " * 25, "**** Nuevamente Guerra!! ****") #mensaje de otra guerra seguida
        self.turno +=1

  def game_play(self):
    self.mazo = Mazo()
    self.mazo.barajar()
    self.jugador_1, self.jugador_2 = self.mazo.repartir()

    while self.turno <= self.max_turnos:
      self.jugar_ronda()

    if self.ganador: #comprobacion de que si hay un ganador o si hay un empate
      print(f"\n                               ***** {self.ganador} gana la partida *****")
    elif self.turno > self.max_turnos:
      print("Limite alcanzado")
      print(" "*25, "***** Empate *****")