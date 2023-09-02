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

    def __len__(self):
        return self.tamanio

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
            antes= actual.anterior
            antes.siguiente = nodo_nuevo
            nodo_nuevo.anterior = antes
            nodo_nuevo.siguiente = actual
            actual.anterior = nodo_nuevo

        else:
             raise ValueError("FUERA DE RANGO")
        self.tamanio +=1

    def extraer(self,posicion=None):
        if posicion == 0:
            actual= self.cabeza
            aux= actual.siguiente
            self.cabeza = aux
            self.cabeza.anterior= None
        
        elif posicion == -1 or posicion == self.tamanio -1 or posicion == None:
            actual = self.cola
            antes= actual.anterior
            self.cola = antes
            antes.siguiente= None
        
        elif 0 < posicion < self.tamanio:
            actual= self.cabeza
            for x in range(posicion):
                actual= actual.siguiente
            antes= actual.anterior
            despues= actual.siguiente
            antes.siguiente= despues
            despues.anterior= antes

        else:
            raise ValueError("FUERA DE RANGO")
        self.tamanio -=1
        return actual.dato

    def copiar(self):
        copia_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia_lista

    def invertir(self):
        final= self.cola
        comienzo= self.cabeza
        while comienzo != final and comienzo.anterior != final:
            comienzo.dato,final.dato = final.dato, comienzo.dato
            final= final.anterior
            comienzo= comienzo.siguiente

    def ordenar(self):
        if self.cabeza is not None and self.cabeza != self.cola:
            self.ordenacion_auxiliar(0, self.tamanio-1)
        else:
            raise IndexError("Lista carente de contenido")

    def ordenacion_auxiliar(self,primero,ultimo):
        if primero < ultimo:
            puntoDivision= self.particion(primero,ultimo)

            self.ordenacion_auxiliar(primero, puntoDivision - 1)
            self.ordenacion_auxiliar(puntoDivision + 1 , ultimo)

    def particion(self,primero,ultimo):
        if primero == 0 and ultimo == self.tamanio - 1:
            pivote= self.cabeza
            nodoIzq= self.cabeza.siguiente
            nodoDer= self.cola
        
        #elif

    def concatenar(self,lista):
        copy2= lista.copiar()

        self.cola.siguiente = copy2.cabeza
        copy2.cabeza.anterior = self.cola
        self.cola = copy2.cola

        self.tamanio += len(lista)

        return self #Se retorna la lista concatenada

    def __add__(self,lista):
        copia= self.copiar()
        return copia.concatenar(lista)

    def __iter__(self):
        aux = self.cabeza
        while aux:
            yield(aux.dato)
            aux = aux.siguiente