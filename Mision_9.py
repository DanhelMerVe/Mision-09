# Danhel Alejandro
# Mision 9 uso de lista


def extraerPares(lista):
    listadePares = []
    if lista ==[]:
        return lista
    else:
        for valor in lista:
            if valor % 2 == 0:
                listadePares.append(valor)
        return listadePares


def extraerMayoresPrevio(lista):
    listaMP=[]
    for valor in range(1, len(lista)):
        if lista[valor] > lista[valor -1]:
            listaMP.append(lista[valor])
    return listaMP

def intercambiarParejas(lista):
    listaParejas = []
    if len(lista) == 0:
        return listaParejas
    if len(lista) % 2 != 0:
        for valor in range(1, len(lista), 2):
            listaParejas.append(lista[valor])
            listaParejas.append(lista[valor - 1])
        if valor % 2 == 1:
            listaParejas.append(lista[valor])
            listaParejas.append(lista[valor + 1])
    return listaParejas


def intercambiarMM(lista):
    if len(lista) > 0:
       lista = []
    else:
        valorMayor = max(lista)
        valorMenor = min(lista)
        mayor = lista.index(valorMayor)
        menor = lista.index(valorMenor)
        lista[mayor] = valorMenor
        lista[menor] = valorMayor
        return lista
    return lista



def promediarCentro(lista):
    listaPromedio = lista
    listaPromedio.sort()
    n = len(listaPromedio)
    lista2 = listaPromedio[1:n-1]
    if n > 2:
        promedio = sum(lista2)//len(lista2)
        return promedio
    else:
        return 0


def calcularEstadistica(lista):
    suma = 0
    if lista == []:
        return (0,0)
    else:
        for n in lista:
            promedio = sum(lista) / len(lista)
            divisor = (n - promedio)**2
            suma += divisor
        dividendo = len(lista)-1
        desviacion = (suma/dividendo)**0.5
        return promedio ,desviacion


def main():
    lista = [1,2,3,2,4,13,14,60,5,8,3,22,44,55]
    print("""Recive""", lista, """regresa""", extraerPares(lista))
    print("""Recive """, lista, """regresa""", extraerMayoresPrevio(lista))
    print("""Recive """, lista, """regresa""", intercambiarParejas(lista))
    print("""Recive """, lista, """regresa""", intercambiarMM(lista))
    print("""Recive """, lista, """regresa""", promediarCentro(lista))
    print("""Recive """, lista, """regresa""", calcularEstadistica(lista))

main()