from listadoble import ListaDobleEnlazada
from random import shuffle

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
palos = ['♠', '♥', '♦', '♣']
class Carta:
    def __init__(self,valores,palos):
        self.valores = valores
        self.palos = palos
    
    def visibilidad(self,visible): #SE DESCONOCE (por ahora) 
        self.visible = visible

    def __str__(self):
        return f"{self.valores}{self.palos}"

class Mazo:
    def __init__(self): #FUNCIONAL (por ahora)
        self.mesa= ListaDobleEnlazada()
        self.mazo = ListaDobleEnlazada()
        for palo in palos:
            for valor in valores:
                self.mazo.agregar_al_final(Carta(valor,palo))
        #print("EL MASO:",self.cartas)
        self.jugador_1= ListaDobleEnlazada()
        self.jugador_2= ListaDobleEnlazada()

    def repartir(self): #FUNCIONAL
        for x,i in enumerate(self.mazo):
            if x >= 26:
                self.jugador_1.agregar_al_final(i)
            else:
                self.jugador_2.agregar_al_final(i)

    def barajar(self): #FUNCIONAL
        cartas_lista = list(self.mazo)
        shuffle(cartas_lista)
        self.mazo = ListaDobleEnlazada() #Se le asigna de nuevo la listadoblementeenlazada para que el metodo tenga sus mismas propiedades
        for carta in cartas_lista:
            self.mazo.agregar_al_final(carta) #😆

    def poner_abajo(self,carta):
        self.mazo.agregar_al_final(carta)

    def poner_arriba(self,carta):
        self.mazo.agregar_al_inicio(carta)

    def extraer_carta(self):
        carta= self.mazo.extraer()
        return carta

class JuegoDeGuerra:
    def __init__(self,limite_turnos=10000):
        self.turno= 0
        self.max_turnos= limite_turnos

    def game_play(self):
        pass
        




A= Mazo()

A.barajar()

A.repartir()

b= A.mazo

aux= A.jugador_1
rodrigo= A.jugador_2

print("JUGADOR1",aux)
print(len(aux))

print("JUGADOR2",rodrigo)
print(len(rodrigo))

# O=aux.extraer_carta()
# print(O)