class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior= None


class Lista_doble_enlace:
    def __init__(self):
        self.primero = None
        self.utimo = None
        self.tamanio= 0

    def esta_vacia(self):
        return self.primero == None

    def agregar_al_final(self,dato):
        if self.esta_vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux=self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior= aux
        self.tamanio += 1


    def agregar_al_inicio(self,dato):
        if self.esta_vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.tamanio += 1

    def iterar_inicio(self):
        aux= self.primero
        while aux != None:
            print(aux.dato)
            aux= aux.siguiente
    
    def iterar_final(self):
        aux= self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior

    def tamanio(self):
        return self.tamanio
        

aux= Lista_doble_enlace()
a= aux.esta_vacia()
print(a)

