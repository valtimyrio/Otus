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


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    if number > 1:
        return True
    else:
        return False


def filter_numbers(lst, filter_type):
    list_res = []
    if filter_type == "odd":
        for number in lst:
            if number % 2 == 1:
                list_res.append(number)
    elif filter_type == "even":
        for number in lst:
            if number % 2 == 0:
                list_res.append(number)
    elif filter_type == "prime":
        for number in lst:
            bool_is_prime = is_prime(number)
            if bool_is_prime:
                list_res.append(number)

    return list_res
