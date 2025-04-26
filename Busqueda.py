def busqueda_binaria_iterativa(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda +1 < derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            izquierda = medio
        else:
            derecha = medio
    if lista[derecha] == objetivo:
        return derecha
    return -1 

def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha):
    if izquierda + 1 >= derecha:
        if lista[izquierda] == objetivo:
            return izquierda
        if lista[derecha] == objetivo:
            return derecha
        return -1

    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio)
    

lista_ordenada = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
objetivo = 100

indice_iterativo = busqueda_binaria_iterativa(lista_ordenada, objetivo)
print("Iterativa: El elemento está en el índice ",indice_iterativo)


indice_recursivo = busqueda_binaria_recursiva(lista_ordenada, objetivo, 0, len(lista_ordenada) - 1)
print("Recursiva: El elemento está en el índice ", indice_recursivo)