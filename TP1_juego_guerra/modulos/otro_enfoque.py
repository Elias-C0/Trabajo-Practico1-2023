from Lista_Enlace.listadoble import ListaDobleEnlazada
from random import shuffle
valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
palos = ['♠', '♥', '♦', '♣']

class Carta:
  def __init__(self,valores,palos):
    self.valores = valores
    self.palos = palos

  def __str__(self):
    return f"{self.valores}{self.palos}"
  
class Mazo:
  def __init__(self):
    self.mazo= ListaDobleEnlazada()

    for palo in palos: #Se le agregan las cartas con los valores y palos al mazo
      for valor in valores:
          self.mazo.agregar_al_final(Carta(valor,palo))

  def barajar(self):
    cartas_lista = list(self.mazo)
    shuffle(cartas_lista)
    print(len(self.mazo))
    self.mazo = ListaDobleEnlazada()
    print(len(self.mazo))
    for carta in cartas_lista:
      self.mazo.agregar_al_final(carta) #😆

  def repartir(self):
    jugador_1 = Mazo()
    jugador_2 = Mazo()
    print("pene",self.mazo)
    print("pene2",len(self.mazo))
    for x,carta in enumerate(self.mazo):
      if x % 2 == 0:
        jugador_1.poner_arriba(carta)
      else:
        jugador_2.poner_arriba(carta)
    print("DSADA",len(jugador_1.mazo))
    print("DS432432ADA",len(jugador_2.mazo))
    return jugador_1, jugador_2

  def poner_arriba(self,carta):
    self.mazo.agregar_al_inicio(carta)

  def poner_abajo(self,carta):
    self.mazo.agregar_al_final(carta)

  def sacar_arriba(self):
    return self.mazo.extraer(0)

class JuegoDeGuerra:
  def __init__(self,limite_turnos=10): # es 10000 pero pongo 10 temporalmente
    self.turno = 1
    self.max_turnos = limite_turnos

  def game_play(self):
    self.mazo= Mazo()
    self.mazo.barajar()
    self.jugador_1, self.jugador_2 = self.mazo.repartir()

    print(self.jugador_1.mazo)
    print(len(self.jugador_1.mazo))

    #print("Jugador 1:", carta_jugador_1)
    while self.turno < self.max_turnos:
      carta_jugador_1 = self.jugador_1.sacar_arriba()
      carta_jugador_2 = self.jugador_2.sacar_arriba()

      print("Jugador 1:", carta_jugador_1)

      if valores.index(carta_jugador_1.valores) > valores.index(carta_jugador_2.valores):
        self.jugador_1.poner_abajo(carta_jugador_1)
        self.jugador_1.poner_abajo(carta_jugador_2)
      else:
          self.jugador_2.poner_abajo(carta_jugador_1)
          self.jugador_2.poner_abajo(carta_jugador_2)

      self.turno +=1

juego = JuegoDeGuerra(limite_turnos=10)  # Puedes ajustar el número de turnos
juego.game_play()
