# def gen_bin(M, prefix=""): # Функция, которая генерирует все числа с лидирующими незначащими нулями только для двоичной системы счисления
#     if M == 0:
#         print(prefix)
#         return
#     for digit in "0", "1":
#         gen_bin(M-1, prefix+digit)

# gen_bin(10)


# def generate_number(N:int, M:int, prefix=None):
#     """ Функция, которая генерирует все числа с лидирующими незначащими нулями 
#         в N ричной системе счисления (N <= 10)
#         длинны M
#     """
#     prefix = prefix or []
#     if M == 0:
#         print(prefix)
#         return
#     for digit in range(N):
#         prefix.append(digit)
#         generate_number(N, M-1, prefix)
#         prefix.pop()

# generate_number(4, 3)


def generate_permutations(N:int, M:int=-1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях, с префиксом prefix """
    M = M if M != -1 else N # По умолчанию N чисел в позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=', ', sep='')
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

def find(number, A):
    """ Ищет number в А и возвращает True, если такое число там есть и False, если такого числа там нет """
    for x in A:
        if number == x:
            return True
        return False

generate_permutations(5)