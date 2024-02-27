# from typing import Callable


# def give_something(text: str) -> str:
#     return text


# def another_function(fn: Callable[[str], str], name: str) -> str:
#     return fn(name)


# a = another_function(give_something, "Albert")

# print(a)

# =================================================================


# def print_dot_a():
#     print("Dot A")

#     def print_dot_b():
#         print("Dot B")

#     def print_dot_c():
#         print("Dot C")

#     print_dot_c()
#     print_dot_b()


# print_dot_a()

# =================================================================


# def get_number(numb: int):

#     def single_digit():
#         return "It is single digit"

#     def multiple_digit():
#         return "It is multiple digit"

#     if numb < 10:
#         return single_digit
#     return multiple_digit


# number_1 = get_number(5)

# print(number_1())

# =================================================================

# from typing import Callable


# def my_decorator(fn: Callable):

#     def wrapper():
#         print("Say something before")
#         result = fn()
#         print("Say something after")
#         return result

#     return wrapper


# @my_decorator
# def say_hello() -> None:
#     print("Hello")


# # me_say = my_decorator(say_hello)
# # me_say()

# say_hello()


# @my_decorator
# def give_two_numbers():
#     return 2


# give_two_numbers()

# =================================================================

from typing import Callable


def my_decorator(fn: Callable):

    def wrapper():
        print("Say something before")
        result = fn()
        print("Say something after")
        return result

    return wrapper


@my_decorator
def give_two_numbers():
    return 2


value = give_two_numbers()

print(value)
