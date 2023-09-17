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
        if posicion == 0: # Si la posición es 0, se extrae el primer nodo
            actual= self.cabeza
            aux= actual.siguiente
            self.cabeza = aux
            if self.cabeza is not None:
                self.cabeza.anterior = None

        
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
        #Se le resta 1 al tamaño de la lista y se devuelve el dato del nodo extraído
        self.tamanio -=1
        return actual.dato

    def copiar(self):
        copia_lista = ListaDobleEnlazada() #Se crea una copia de la lista
        actual = self.cabeza #Se asigna a actual el comienzo de la lista original
        while actual != None:
            copia_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente #Se mueve al siguiente nodo
        return copia_lista

    def invertir(self):
        #Inicializamos dos punteros, uno al final y otro al comienzo.
        final= self.cola
        comienzo= self.cabeza
        while comienzo != final and comienzo.anterior != final: 
            comienzo.dato,final.dato = final.dato, comienzo.dato #Intercambiamos los datos entre los nodos de comienzo y final.
            final= final.anterior #Movemos el puntero un nodo hacia atrás
            comienzo= comienzo.siguiente #Movemos el puntero un nodo hacia delante.

    def ordenar(self):
        if self.cabeza is not None and self.cabeza != self.cola: # Verificamos si la lista no está vacía y si tiene más de un elemento
            self.ordenacion_auxiliar(0, self.tamanio-1) #Se llama a la función "ordenacion_auxiliar" con los índices del primer y último elemento
        else:
            raise IndexError("Lista carente de contenido")

    def ordenacion_auxiliar(self,primero,ultimo):
        if primero < ultimo: # Comprueba si hay mas de un elemento en el rango especificado
            puntoDivision= self.particion(primero,ultimo)
            #Se divide la lista y ordena cada mitad
            self.ordenacion_auxiliar(primero, puntoDivision - 1)
            self.ordenacion_auxiliar(puntoDivision + 1 , ultimo)

    def particion(self,primero,ultimo):
        #Aca se establecen los nodos pivote, nodoIzq y nodoDer dependiendo de los índices primero y último
        if primero == 0 and ultimo == self.tamanio -1:
            pivote= self.cabeza
            nodoIzq= self.cabeza.siguiente
            nodoDer= self.cola

        elif (self.tamanio // 2) > primero:
            pivote = self.cabeza
            for x in range(primero):
                pivote= pivote.siguiente
            nodoIzq = pivote.siguiente

        else:
            pivote = self.cola
            for x in range(((self.tamanio - 1) - primero)):
                pivote= pivote.anterior
            nodoIzq= pivote.siguiente

        if ultimo > (self.tamanio/2):
            nodoDer= self.cola
            for x in range(((self.tamanio - 1) - ultimo)):
                nodoDer = nodoDer.anterior

        else:
            nodoDer= self.cabeza
            for x in range(ultimo):
                nodoDer= nodoDer.siguiente


        suceso=False
        marcaIzq= primero + 1
        marcaDer= ultimo

        while not suceso:
            while marcaIzq <= marcaDer and nodoIzq.dato <= pivote.dato:
                nodoIzq= nodoIzq.siguiente
                marcaIzq += 1

            while marcaDer >= marcaIzq and nodoDer.dato >= pivote.dato:
                nodoDer= nodoDer.anterior
                marcaDer -=1

            if marcaIzq > marcaDer:
                suceso=True

            else:
                aux= nodoIzq.dato
                nodoIzq.dato= nodoDer.dato
                nodoDer.dato= aux
        #Intercambiamos los datos del pivote y el nodoDer
        temporal= pivote.dato
        pivote.dato= nodoDer.dato
        nodoDer.dato= temporal

        return marcaDer
    
    def concatenar(self,lista):
        if self.cabeza is None or lista is None:
            raise ValueError("Una lista esta vacia")
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
        aux = self.cabeza # Se le asigna el primer nodo de la lista.
        while aux:
            yield(aux.dato) #'yield' se usa para hacer de esta función un generador
            aux = aux.siguiente

    def __str__(self): #importante para la visualizacion de las cartas en juego de guerra
        string = ""
        nodo = self.cabeza
        while nodo != None:
            string += str(nodo.dato)
            string += " "
            nodo = nodo.siguiente
        return string