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

  def sacar_arriba(self):
    if not self.mazo.esta_vacia():
      return self.mazo.extraer(0)
    else:
      return None
  
  def __iter__(self):
    return iter(self.mazo)

class JuegoDeGuerra:
  def __init__(self,limite_turnos=1000): # es 10000 pero pongo 100 temporalmente
    self.turno = 1
    self.max_turnos = limite_turnos

  def game_play(self):
    self.mazo= Mazo()
    self.mazo.barajar()
    self.jugador_1, self.jugador_2 = self.mazo.repartir()

    while self.turno <= self.max_turnos:
        carta_jugador_1 = self.jugador_1.sacar_arriba()
        carta_jugador_2 = self.jugador_2.sacar_arriba()
        
        if not carta_jugador_1 or not carta_jugador_2:
            if len(self.jugador_1.mazo) > len(self.jugador_2.mazo):
              print("\n                               ***** Jugador 1 gana la partida *****")
            elif len(self.jugador_2.mazo) > len(self.jugador_1.mazo):
              print("\n                               ***** Jugador 2 gana la partida *****")
            else:
              print("                                          ***** Empate *****")
            break
        
        print("\n-------------------------------------")
        
        print(f"Turno: {self.turno}")
        
        print("Jugador 1:")
        for i, carta in enumerate(self.jugador_1.mazo, 1):
          print("-X ", end=" ")
          if i % 10 == 0:
            print()
        print()
        print("\n")
        
        print(f"         {carta_jugador_1} {carta_jugador_2}\n")
       
        print("Jugador 2:")
        for i, carta in enumerate(self.jugador_2.mazo, 1):
          print("-X ", end=" ")
          if i % 10 == 0:
            print()
        print()

        if (valores.index(carta_jugador_1.valores)+2) > (valores.index(carta_jugador_2.valores)+2):
          self.jugador_1.poner_abajo(carta_jugador_1)
          self.jugador_1.poner_abajo(carta_jugador_2)
          print("\nJugador 1 gana la ronda")

        elif (valores.index(carta_jugador_1.valores)+2) < (valores.index(carta_jugador_2.valores)+2):
          self.jugador_2.poner_abajo(carta_jugador_1)
          self.jugador_2.poner_abajo(carta_jugador_2)
          print("\nJugador 2 gana la ronda")

        else:
          print("\n-------------------------------------")
          print("                                      **** Guerra!! ****                                      ")
          self.jugador_1.poner_arriba(carta_jugador_1)
          self.jugador_2.poner_arriba(carta_jugador_2)
          self.guerra()

        self.turno += 1

    if self.turno == self.max_turnos:
      print("                                          ***** Empate *****                                          ")

  def guerra(self):
     self.turno+=1
     botin= Mazo()
     
     if len(self.jugador_1.mazo) < 4 or len(self.jugador_2.mazo) < 4:
       print("\n No hay las suficientes cartas para seguir haciendo la guerra")
       if len(self.jugador_1.mazo) > len(self.jugador_2.mazo):
         print("\n                               ***** jugador 1 gana la partida*****                     ")
       elif len(self.jugador_1.mazo) < len(self.jugador_2.mazo):
         print("\n                               ***** jugador 2 gana la partida*****                     ")
       else:
         self.turno= self.max_turnos +1
       return
     
     carta_jugador_1 = self.jugador_1.sacar_arriba()
     carta_jugador_2 = self.jugador_2.sacar_arriba()
     
     if carta_jugador_1 is None or carta_jugador_2 is None:
        print("\n No hay suficientes cartas para seguir haciendo la guerra")
        if len(self.jugador_1.mazo) > len(self.jugador_2.mazo):
            print("\n                               ***** Jugador 1 gana la partida *****")
        elif len(self.jugador_1.mazo) < len(self.jugador_2.mazo):
            print("\n                               ***** Jugador 2 gana la partida *****")
        else:
            self.turno = self.max_turnos + 1
        return

     botin.poner_abajo(carta_jugador_1)
     botin.poner_abajo(carta_jugador_2)
     for x in range(3):
       carta1= self.jugador_1.sacar_arriba()
       carta2= self.jugador_2.sacar_arriba()
       if carta1 is not None:
        botin.poner_abajo(carta1)
       if carta2 is not None:
        botin.poner_abajo(carta2)
    
     carta_jugador_guerra_1= self.jugador_1.sacar_arriba()
     carta_jugador_guerra_2= self.jugador_2.sacar_arriba()
     
     if len(self.jugador_1.mazo) < 4 or len(self.jugador_2.mazo) < 4:
       print("\n No hay las suficientes cartas para seguir haciendo la guerra")
       if len(self.jugador_1.mazo) > len(self.jugador_2.mazo):
         print("\n                               ***** jugador 1 gana la partida*****                     ")
       elif len(self.jugador_1.mazo) < len(self.jugador_2.mazo):
         print("\n                               ***** jugador 2 gana la partida*****                     ")
       else:
         self.turno=self.max_turnos + 1
         return
  
     print(f"Turno: {self.turno}")
     
     print("Jugador 1:")
     for i, carta in enumerate(self.jugador_1.mazo, 1):
          print("-X ", end=" ")
          if i % 10 == 0:
            print()
     print()
     print("\n")
     
     print(f"         {carta_jugador_1} {carta_jugador_2}", end=" ")
     print("-X " * 6, end="")
     print(f"{carta_jugador_guerra_1} {carta_jugador_guerra_2}")
     print("\n")
     print("Jugador 2:")
     for i, carta in enumerate(self.jugador_2.mazo, 1):
          print("-X ", end=" ")
          if i % 10 == 0:
            print()
     print()
     

     if (valores.index(carta_jugador_guerra_1.valores)+2) > (valores.index(carta_jugador_guerra_2.valores)+2):
        for x in botin:
          self.jugador_1.poner_abajo(x)
        self.jugador_1.poner_abajo(carta_jugador_guerra_1)
        self.jugador_1.poner_abajo(carta_jugador_guerra_2)
        print("\nJugador 1 gana la ronda")

     elif (valores.index(carta_jugador_guerra_1.valores)+2) < (valores.index(carta_jugador_guerra_2.valores)+2):
        for x in botin:  
          self.jugador_2.poner_abajo(x)
        self.jugador_2.poner_abajo(carta_jugador_guerra_1)
        self.jugador_2.poner_abajo(carta_jugador_guerra_2)
        print("\nJugador 2 gana la ronda")

     else:
        print("\n-------------------------------------")
        print("                                      **** Guerra!! ****                                      ")
        self.guerra()

     self.turno += 1
     if self.turno == self.max_turnos:
      print("                                          ***** Empate *****                                          ")

juego = JuegoDeGuerra()
juego.game_play()

#falta arreglar la declaracion del ganador