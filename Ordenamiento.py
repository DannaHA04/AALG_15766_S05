array = [2,8,5,3,9,4,1]

def ordSeleccion(array):
    n = len(array)

    for mano in range(n - 1):
        posmin = mano
        for ojo in range(mano + 1, n):
            if array[ojo] < array[posmin]:
                posmin = ojo
            array[mano], array[posmin] = array[posmin], array[mano]

ordSeleccion(array)
print("Lista ordenada por seleccion:", array)


def ordBurbuja(array):
    N = len(array)
    for i in range(1, N):
        for j in range(0, N - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

ordBurbuja(array)
print("Lista ordenada por burbuja:", array)


def ordInsercion(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1

ordInsercion(array)
print("Lista ordenada por Insercion:", array)