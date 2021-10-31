def merge(A:list, B:list):
    """ Функция, которая производит слияние двух массивов в один """
    C = [0] * (len(A) + len(B))
    i=k=n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]; i += 1; n += 1
        else:
            C[n] = B[k]; k += 1; n += 1
    while i < len(A):
        C[n] = A[i]; i += 1; n += 1
    while k < len(B):
        C[n] = B[k]; k += 1; n += 1
    return C


def merge_sort(A):
    """ Рекурсивная функция сортировки """
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)] # Левая половинка
    R = [A[i] for i in range(middle, len(A))] # Правая половинка
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]



def hoar_sort(A):
    """ Алгоритм сортировки Тони Хоара """
    if len(A) <= 1:
        return
    barrier = A[0] # Выбираем барьерный элемент, с которым будем сравнивать все остальные
    L = []; M = []; R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L+M+R:
        A[k] = x; k += 1