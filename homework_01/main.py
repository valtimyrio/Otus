"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: x * x, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(lst, type):
    list_res = []
    if type == "odd":
        for a in lst:
            if a % 2 == 1:
                list_res.append(a)
    elif type == "even":
        for a in lst:
            if a % 2 == 0:
                list_res.append(a)
    elif type == "prime":
        for a in lst:
            f = True
            for i in range(2, a):
                if a % i == 0:
                    f = False
                    break
            if f == True and a > 1:
                list_res.append(a)

    return list_res
