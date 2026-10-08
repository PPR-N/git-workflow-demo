from typing import Union

Number = Union[int, float]


def calculate_sum(a: Number, b: Number) -> Number:
    """Return the sum of two numbers.

    :param a: first addend
    :param b: second addend
    :return: the sum of a and b
    """
    return a + b


def calculate_product(a: Number, b: Number) -> Number:
    """Return the product of two numbers.

    :param a: first factor
    :param b: second factor
    :return: the product of a and b
    """
    return a * b


def calculate_difference(a, b):
    return a - b


if __name__ == '__main__':
    print('Sum:', calculate_sum(10, 20))
    print('Product:', calculate_product(10, 20))
    print('Difference:', calculate_difference(20, 10))
