def array_search(A:list, N:int, x:int):
    """
        Осуществляет поиск числа х в массиве А
        от 0 до N-1 индекса включительно.
        Возвращает индекс элемента х в массиве А.
        Или -1, если такого элемента нет в массиве.
        А если есть два одинаковых элемента, то возвращает
        первый попавшийся.
    """
    for i in range(N):
        if A[i] == x:
            return i
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5, 6, 7]
    m = array_search(A1, 7, 6)
    if m == 5:
        print('test1 - ok')
    else:
        print('test1 - fail')

    A2 = [-2, 2, 6, 12, 25, 30, 45]
    m = array_search(A2, 7, 3)
    if m == -1:
        print('test2 - ok')
    else:
        print('test2 - fail')

    A3 = [-2, 2, 6, 2, 25, 30, 45]
    m = array_search(A3, 7, 2)
    if m == 1:
        print('test3 - ok')
    else:
        print('test3 - fail')

test_array_search()




def invert_array(A:list, N:int):
    """
        Обращение массива, т.е. поворот задом наперед
        в рамках индексов от 0 до N-1
    """
    for i in range(N//2):
        A[N-1-i], A[i] = A[i], A[N-1-i]

def test_invert_array():
    A1 = [0, 1, 2, 3, 4, 5, 6, 7]
    print(A1)
    invert_array(A1, 8)
    print(A1)
    if A1 == [7, 6, 5, 4, 3, 2, 1, 0]:
        print('test1 - ok')
    else:
        print('test1 - fail')


    A2 = [0, 0, 0, 0, 0, 0, 0, 11]
    print(A2)
    invert_array(A2, 8)
    print(A2)
    if A2 == [11, 0, 0, 0, 0, 0, 0, 0]:
        print('test2 - ok')
    else:
        print('test2 - fail')

test_invert_array()


A = [1, 2, 4, 5, 7, 10, 12, 22, 31, 34] 
B = [x**3 for x in A if x%2 == 0] # Тренировка записи короткого создания массива, а так же тернарный оператор
print(B)