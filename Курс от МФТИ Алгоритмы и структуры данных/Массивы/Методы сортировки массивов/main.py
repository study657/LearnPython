def insert_sort(A:list):
    """ Сортировка списка А алгоритмом "вставки (insert sert)" """
    N = len(A) # Получили кол-во элементов в массиве
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choose_sert(A:list):
    """ Сортировка списка А алгоритмом "Выбора" """
    N = len(A) # Получили кол-во элементов в массиве
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    """ Сортировка списка А алгоритмом "Пузарька" """
    N = len(A) # Получили кол-во элементов в массиве
    for bypass in range(1, N): # bypass - проход
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]



# Функция для тестирования вышеупомянутых алгоритмов
def test_sort(sort_algoritm):
    print('Тестируем: ', sort_algoritm.__doc__) # sort_algoritm.__doc__ - позволяет нам вывести техническую инструкцию к функции, если таковая написана
    print('testcase №1: ', end='') # Метод end позволяет указать нам что делать после напечатания, в данном случае мы запрещаем перенос строки
    A = [4, 5, 2, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algoritm(A)
    print('Ok' if A == A_sorted else print('Fail')) # Тернарный оператор (короткая запись)

    print('testcase №2: ', end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20)) # Создат список, который сгенерирует прогрессию от 0 до 19
    sort_algoritm(A)
    print('Ok' if A == A_sorted else print('Fail')) # Тернарный оператор (короткая запись)
    
    print('testcase №3: ', end='') # Метод end позволяет указать нам что делать после напечатания, в данном случае мы запрещаем перенос строки
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algoritm(A)
    print('Ok' if A == A_sorted else print('Fail')) # Тернарный оператор (короткая запись)

test_sort(insert_sort)
test_sort(choose_sert)
test_sort(bubble_sort)