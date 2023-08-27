class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior= None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio= 0

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
        self.tamanio += 1

    def agregar_al_final(self,dato):
        if self.esta_vacia():
            self.cabeza = self.cola = Nodo(dato)
        else:
            aux= self.cola
            self.cola = aux.siguiente = Nodo(dato)
            self.cola.anterior= aux
        self.tamanio += 1

    def insertar(self,dato,posicion=None):
        nodo_nuevo= Nodo(dato)
        if self.esta_vacia(): #en caso que la lista este vacia
            self.cabeza = self.cola = nodo_nuevo
        
        elif posicion is None or posicion == self.tamanio: #el dato se inserta al final
            self.cola.siguiente = nodo_nuevo
            nodo_nuevo.anterior = self.cola
            self.cola = nodo_nuevo

        elif posicion == 0: # el dato se inserta al principio
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nodo_nuevo
            self.cabeza = nodo_nuevo

        elif posicion > 0 and posicion < self.tamanio:
            actual = self.cabeza
            for x in range(posicion):
                actual= actual.siguiente
            after= actual.anterior
            after.siguiente = nodo_nuevo
            nodo_nuevo.anterior = after
            nodo_nuevo.siguiente = actual
            actual.anterior = nodo_nuevo

        else:
             raise ValueError("FUERA DE RANGO")
        self.tamanio +=1

    def __iter__(self):
        aux = self.cabeza
        while aux:
            yield(aux.dato)
            aux = aux.siguiente

    def __len__(self):
        return self.tamanio
    
    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia_lista
    