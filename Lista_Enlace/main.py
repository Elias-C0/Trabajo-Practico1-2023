from listadoble import ListaDobleEnlazada

aux= ListaDobleEnlazada()

aux.agregar_al_inicio(32)
aux.agregar_al_final(71)
aux.agregar_al_final(2)
aux.agregar_al_final(29)
aux.agregar_al_final(47)
aux.agregar_al_final(-139)
aux.agregar_al_final(-75)
aux.agregar_al_final(121)
aux.agregar_al_final(25)

aux.ordenar()

for x in aux:
    print(x)