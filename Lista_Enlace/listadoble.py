class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior= None


class Lista_doble_enlace:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio= 0

    def esta_vacia(self):
        return self.cabeza == None

    def agregar_al_final(self,dato):
        if self.esta_vacia():
            self.cabeza = self.cola = Nodo(dato)
        else:
            aux=self.cola
            self.cola = aux.siguiente = Nodo(dato)
            self.cola.anterior= aux
        self.tamanio += 1

    def agregar_al_inicio(self,dato):
        if self.esta_vacia():
            self.cabeza = self.cola = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.cabeza
            self.cabeza.anterior = None
            self.cabeza = aux
        self.tamanio += 1

    def iterar_inicio(self):
        aux= self.cabeza
        while aux != None:
            print(aux.dato)
            aux= aux.siguiente
    
    def iterar_final(self):
        aux= self.cola
        while aux:
            print(aux.dato)
            aux = aux.anterior

    def tamanio(self):
        return self.tamanio
    
    def copiar_lista(self):
        copia_lista = Lista_doble_enlace()
        actual = self.cabeza
        while actual:
            copia_lista.agregar(actual.dato)
            actual = actual.siguiente
        return copia_lista
    
aux= Lista_doble_enlace()
a= aux.esta_vacia()
print(a)

