from Lista_Enlace.listadoble import ListaDobleEnlazada
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
    self.mazo= ListaDobleEnlazada()

  def generar_mazo(self):
    for palo in palos: #Se le agregan las cartas con los valores y palos al mazo
      for valor in valores:
          self.mazo.agregar_al_final(Carta(valor,palo))

  def barajar(self):
    self.generar_mazo()
    cartas_lista = list(self.mazo)
    shuffle(cartas_lista)
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
        print(f"El jugador {jugador} se quedó sin cartas para continuar con la guerra")
        print(f"\n                               ***** Jugador {otro_jugador} gana la partida *****")
        exit(1)
  
  def __iter__(self):
    return iter(self.mazo)

class JuegoDeGuerra:
  def __init__(self, limite_turnos=10000):
    self.turno = 1
    self.max_turnos = limite_turnos
    self.ganador = None

  def imprimir_mazo(self,jugador):
    for x in range(1,len(jugador.mazo)):
      print("-X ", end=" ")
      if x % 10 == 0:
        print()
    print()

  def jugar_ronda(self):
    carta_jugador_1 = self.jugador_1.sacar_arriba(1)
    carta_jugador_2 = self.jugador_2.sacar_arriba(2)

    if carta_jugador_1 is None or carta_jugador_2 is None:
      if len(self.jugador_1.mazo) > len(self.jugador_2.mazo):
        self.ganador = "Jugador 1"
      elif len(self.jugador_2.mazo) > len(self.jugador_1.mazo):
        self.ganador= "Jugador 2"

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
      print("\nJugador 1 gana la ronda")

    elif valor_carta_jugador_1 < valor_carta_jugador_2:
      self.jugador_2.poner_abajo(carta_jugador_1)
      self.jugador_2.poner_abajo(carta_jugador_2)
      print("\nJugador 2 gana la ronda")

    else:
      print("\n-------------------------------------")
      print(" " *25, "**** Nuevamente Guerra!! ****")
      self.jugador_1.poner_arriba(carta_jugador_1)
      self.jugador_2.poner_arriba(carta_jugador_2)
      self.guerra()

    self.turno += 1
  
  def guerra(self):
    self.turno +=1
    botin=Mazo()
    
    if len(self.jugador_1.mazo) < 4 or len(self.jugador_2.mazo) < 4:
      if len(self.jugador_1.mazo) < 4:
        self.ganador = "Jugador 2"
        print("El Jugador 1 no tiene suficientes cartas para continuar la guerra")
      elif len(self.jugador_2.mazo) < 4:
        self.ganador = "Jugador 1"
        print("El Jugador 2 no tiene suficientes cartas para continuar la guerra")
      else:
        self.turno = self.max_turnos + 1

    carta_jugador_1 = self.jugador_1.sacar_arriba(1)
    carta_jugador_2 = self.jugador_2.sacar_arriba(2)
    botin.poner_abajo(carta_jugador_1)
    botin.poner_abajo(carta_jugador_2)

    for h in range(3):
      carta1 = self.jugador_1.sacar_arriba(1)
      carta2 = self.jugador_2.sacar_arriba(2)

      if carta1 is not None:
        botin.poner_abajo(carta1)
      else:
        self.ganador = "Jugador 2"
        self.turno = self.max_turnos + 1 # sirve para finalizar la partida cuando, en este caso, el jugador 1 no cuenta con mas cartas

      if carta2 is not None:
        botin.poner_abajo(carta2)
      else:
        self.ganador = "Jugador 1"
        self.turno = self.max_turnos + 1

    carta_jugador_guerra_1 = self.jugador_1.sacar_arriba(1)
    carta_jugador_guerra_2 = self.jugador_2.sacar_arriba(2)

    print(f"Turno: {self.turno}")
    print("Jugador 1:")
    self.imprimir_mazo(self.jugador_1)
    print()
    print(f"         {carta_jugador_1} {carta_jugador_2}", end=" ")
    print("-X " * 6, end="")
    print(f"{carta_jugador_guerra_1} {carta_jugador_guerra_2}")
    print("\n")
    print("Jugador 2:")
    self.imprimir_mazo(self.jugador_2)

    valor_carta_guerra_1 = valores.index(carta_jugador_guerra_1.valores) + 2
    valor_carta_guerra_2 = valores.index(carta_jugador_guerra_2.valores) + 2

    if valor_carta_guerra_1 > valor_carta_guerra_2:
      for x in botin:
        self.jugador_1.poner_abajo(x)
      self.jugador_1.poner_abajo(carta_jugador_guerra_1)
      self.jugador_1.poner_abajo(carta_jugador_guerra_2)
      print("\nJugador 1 gana la ronda")

    elif valor_carta_guerra_1 < valor_carta_guerra_2:
      for x in botin:
        self.jugador_2.poner_abajo(x)
      self.jugador_2.poner_abajo(carta_jugador_guerra_1)
      self.jugador_2.poner_abajo(carta_jugador_guerra_2)
      print("\nJugador 2 gana la ronda")

    else:
      print("\n-------------------------------------")
      print(" " * 25, "**** Nuevamente Guerra!! ****")
      botin.poner_abajo(carta_jugador_guerra_1)
      botin.poner_abajo(carta_jugador_guerra_2)

  def game_play(self):
    self.mazo = Mazo()
    self.mazo.barajar()
    self.jugador_1, self.jugador_2 = self.mazo.repartir()

    while self.turno <= self.max_turnos:
      self.jugar_ronda()

    if self.ganador:
      print(f"\n                               ***** {self.ganador} gana la partida *****")
    elif self.turno > self.max_turnos:
      print("Limite alcanzado")
      print(" "*25, "***** Empate *****") 

juego = JuegoDeGuerra()
juego.game_play()