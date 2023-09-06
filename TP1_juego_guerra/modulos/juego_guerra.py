from Lista_Enlace.listadoble import ListaDobleEnlazada
from random import shuffle

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
palos = ['♠', '♥', '♦', '♣']
class Carta:
    def __init__(self,valores,palos):
        self.valores = valores
        self.palos = palos
    
    # def visibilidad(self,visible): #SE DESCONOCE (por ahora) 
    #     self.visible = visible

    def __str__(self):
        return f"{self.valores}{self.palos}"
    
class Mazo:
    def __init__(self): #FUNCIONAL (por ahora)
        self.mazo = ListaDobleEnlazada() #Se le asigna de nuevo la listadoblementeenlazada para que el metodo tenga sus mismas propiedades
        self.jugador_1= ListaDobleEnlazada()
        self.jugador_2= ListaDobleEnlazada()
        
        for palo in palos:
            for valor in valores:
                self.mazo.agregar_al_final(Carta(valor,palo))
 
        #print("EL MASO:",self.cartas)


    def repartir(self): #FUNCIONAL
        for x,carta in enumerate(self.mazo):
            if x % 2 == 0:
                self.jugador_1.agregar_al_final(carta)
            else:
                self.jugador_2.agregar_al_final(carta)

    def barajar(self): #FUNCIONAL
        cartas_lista = list(self.mazo)
        shuffle(cartas_lista)
        for carta in cartas_lista:
            self.mazo.agregar_al_final(carta) #😆

    def poner_arriba(self,carta):
        self.mazo.agregar_al_inicio(carta)

    def poner_abajo(self,jugador,carta):
        self.mazo.agregar_al_final(carta)

    def sacar_arriba(self):
        return self.mazo.extraer(0)

class JuegoDeGuerra:
    def __init__(self,limite_turnos=10): # es 10000 pero pongo 10 temporalmente
        self.turno= 1
        self.max_turnos= limite_turnos

    def game_play(self):
        self.mazo = Mazo()
        self.mazo.barajar()
        self.mazo.repartir()

        print("Jugador 1:",self.mazo.jugador_1)
        print("Jugador 2:",self.mazo.jugador_2)

        while self.turno < self.max_turnos:
            carta_jugador_1= self.mazo.jugador_1.extraer(0)
            carta_jugador_2= self.mazo.jugador_2.extraer(0)

            if valores.index(carta_jugador_1.valores) > valores.index(carta_jugador_2.valores):
                self.mazo.poner_abajo(self.mazo.jugador_1, carta_jugador_1)
                self.mazo.poner_abajo(self.mazo.jugador_1, carta_jugador_2)
            else:
                self.mazo.poner_abajo(self.mazo.jugador_2, carta_jugador_1)
                self.mazo.poner_abajo(self.mazo.jugador_2, carta_jugador_2)

            print("-------------------------------------")
            print(f"Turno:{self.turno}")
            print("Jugador 1:")

            print(self.mazo.jugador_1)
            print(carta_jugador_1)

            
            print("Jugador 2:")
            print(self.mazo.jugador_2)
            print(carta_jugador_2)

            if valores.index(carta_jugador_1.valores) == valores.index(carta_jugador_2.valores):

                guerra= "**** Guerra!! ****"
                print(f"{guerra.center(60)}")


            self.turno +=1
        

# A= Mazo()

# A.barajar()

# A.repartir()

# b= A.mazo

# aux= A.jugador_1
# rodrigo= A.jugador_2

# print("JUGADOR1",aux)
# print(len(aux))

# print("JUGADOR2",rodrigo)
# print(len(rodrigo))

b= JuegoDeGuerra()
b.game_play()



# O=aux.extraer_carta()
# print(O)