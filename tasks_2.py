# 1. Write a decorator that should check if all arguments passed to the method are positive.
# If not, it should raise a ValueError. A function should calculate square of numbers.


# from typing import Callable


# def positive(fn: Callable):

#     def wrapper(*args, **kwargs):
#         for x in args:
#             if x < 0:
#                 raise ValueError("Only positives, sorry")
#         my_func = fn(*args, **kwargs)
#         return my_func

#     return wrapper


# @positive
# def square(number: int) -> int:
#     return pow(number, 2)


# print(square(4))


# 2. Write a decorator that catches any exceptions thrown by the function and prints an error message instead of letting the program crash.


# from typing import Callable


# def error_hunter(fn: Callable):

#     def wrapper(*args, **kwargs):
#         try:
#             result = fn(*args, **kwargs)
#             return result
#         except Exception as err:
#             print(f"Error: {err}")

#     return wrapper


# @error_hunter
# def divide_by_zero(number: int):
#     return number / 0


# print(divide_by_zero(4))

# 3. Write a decorator that retries a function if it raises an exception. The function should be retried 3 times before finally raising the exception.

from typing import Callable


def error_hunter(fn: Callable):

    def wrapper(*args, **kwargs):
        counter = 0
        for _ in range(3):
            try:
                result = fn(*args, **kwargs)
                return result
            except Exception:
                pass
            counter += 1
            print(counter)
        return fn(*args, **kwargs)

    return wrapper


@error_hunter
def divide_by_zero(number: int):
    return number / 0


print(divide_by_zero(4))
