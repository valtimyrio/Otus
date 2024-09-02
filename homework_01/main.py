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
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    if flag and number > 1:
        return number


def filter_numbers(lst, filter_type):
    list_res = []
    if filter_type == "odd":
        for a in lst:
            if a % 2 == 1:
                list_res.append(a)
    elif filter_type == "even":
        for a in lst:
            if a % 2 == 0:
                list_res.append(a)
    elif filter_type == "prime":
        for number in lst:
            is_prime_value = is_prime(number)
            if is_prime_value is not None:
                list_res.append(is_prime_value)

    return list_res
