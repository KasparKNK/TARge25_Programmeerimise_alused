"""Function examples."""


def func():
    print("I'm inside the function")


def my_name_is(name):
    print("My name is " + name)

def sum_six(num: int) -> int:
    return 6 + num

def sum_numbers(a, b: int) -> int:
    return a + b


def usd_to_eur(usd: int) -> int:
    return  usd / 1.25