with open ("datos.txt", "r") as archivo:
    todo= archivo.readlines()

def ordenamineto_por_mezcla(lista):
    if len(todo) > 1:
        mitad= len(todo)//2
        mitad_Izq= todo[:mitad]
        mitad_Der= todo[mitad:]

        ordenamineto_por_mezcla(mitad_Izq)
        ordenamineto_por_mezcla(mitad_Der)

        x= 0
        y= 0
        z= 0
        while x < len(mitad_Izq) and y < len(mitad_Der):
            if mitad_Izq[x] < mitad_Der[y]:
                todo[z]= mitad_Izq[x]
                x+=1
            else:
                todo[z]= mitad_Der[y]
                y+=1
            z+=1

        while x < len(mitad_Izq):
            todo[z]= mitad_Izq[x]
            x+=1
            z+=1
        
        while y < len(mitad_Der):
            todo[z]= mitad_Der[y]
            y+=1
            z+=1

resultado= ordenamineto_por_mezcla(todo)
todo=todo.sort()
for x1 in todo:
    for x2 in resultado:
        if x1 == x2:
            pass
        else:
            print("Error en ordenar")

#este es el codigo que me rompió la compu, NO LO PRUEBES
#          NO PROBAR ESTA EN MANTENIMIENTO