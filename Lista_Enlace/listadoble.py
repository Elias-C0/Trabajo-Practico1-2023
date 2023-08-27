class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior= None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano= 0

    def esta_vacia(self):
        return self.cabeza == None

    def agregar_al_inicio(self,dato):
        if self.esta_vacia():
            self.cabeza = self.cola = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.cabeza
            self.cabeza.anterior = aux
            self.cabeza = aux
        self.tamano += 1

    def agregar_al_final(self,dato):
        if self.esta_vacia():
            self.cabeza = self.cola = Nodo(dato)
        else:
            aux= self.cola
            self.cola = aux.siguiente = Nodo(dato)
            self.cola.anterior= aux
        self.tamano += 1

    #REVISAR
    def insertar(self,dato,posicion=None):
        if self.esta_vacia():
            self.cabeza = self.cola = Nodo(dato)
        elif posicion < 0 or posicion > self.tamano:
            raise ValueError("FUERA DE RANGO")
        elif posicion == self.tamano:
            self.agregar_al_final(dato)
        self.tamano +=1

    def __iter__(self):
        aux = self.cabeza
        while aux:
            yield(aux.dato)
            aux = aux.siguiente

    def __len__(self):
        return self.tamano
    
    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia_lista
    