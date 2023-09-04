from listadoble import ListaDobleEnlazada
from random import shuffle 

class Carta:
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']
    def __init__(self,valores,palos):
        self.valores = valores
        self.palos = palos
        #self.visible = False
    
    def visibilidad(self,visible):    
        self.visible = visible

    def __str__(self):
        return f"{self.valores}{self.palos}"

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()
        for palos in Carta.palos:
            for valores in Carta.valores:
                self.cartas.agregar_al_final(Carta(valores,palos))
        
        self.jugador_1= ListaDobleEnlazada()
        self.jugador_2= ListaDobleEnlazada()

    def repartir(self):
        for x in range(26):
            carta = self.cartas[x]
            carta.visibilidad(False)
            self.jugador_1.agregar_al_final(carta)

        for i in range(26,52):
            carta = self.cartas[i]
            carta.visibilidad(False)
            self.jugador_2.agregar_al_final(carta)

    def barajar(self):
        shuffle(self.cartas)

    def poner_abajo(self,jugador_ganador):
        for cartas in self.mesa:
            cartas.visibilidad = True
        jugador_ganador.agregar_al_final(cartas)

    def poner_arriba(self,jugador_ganador):
        for cartas in self.mesa:
            cartas.visibilidad = False
        jugador_ganador.agregar_al_final(cartas)

class JuegoGuerra:
  
    def __init__(self,numeroJugadas):
        self.cantidad_jugadas= numeroJugadas
        self.mesa= ListaDobleEnlazada()

    def comenzar_game(self):
        for turno in range(self.cantidad_jugadas):
            print("Turno", turno +1)
            self.realizar_turno()

        if self.ganador():
            print("HAY UN GANADOR")
        
        else:
            print("termina en empate")

    def realizar_turno(self):
        carta_jugador1= self.jugador_1.extraer()
        carta_jugador2= self.jugador_2.extraer()

        print(f"Carta jugador 1: {carta_jugador1}")
        print(f"Carta jugador 2: {carta_jugador2}")

        self.mesa.agregar_al_final(carta_jugador1)
        self.mesa.agregar_al_final(carta_jugador2)

        if carta_jugador1 > carta_jugador2:
            self.jugador_1.agregar_al_final(self.mesa)
            self.mesa = ListaDobleEnlazada()
            print("Turno ganado por jugador 1")
        
        elif carta_jugador2 > carta_jugador1:
            self.jugador_2.agregar_al_final(self.mesa)
            self.mesa = ListaDobleEnlazada()
            print("Turno ganado por jugador 2")

        print("Estado de los mazos y la mesa después del turno:")
        print(f"Mazo jugador 1: {self.jugador_1}")
        print(f"Mazo jugador 2: {self.jugador_2}")
        print(f"Cartas en la mesa: {self.mesa}")
        
        # else:
        #     pass


if __name__ == "__main__":
    numero_jugadas = 10  # Define el número máximo de jugadas
    juego = JuegoGuerra(numero_jugadas)

    # Configura los mazos y jugadores aquí...

    # Inicia el juego
    juego.comenzar_game()