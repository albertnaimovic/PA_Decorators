# from typing import Callable


# def repeat(num_of_times: int):
#     def repeat_decorator(fn: Callable) -> str:
#         def wrapper(*args, **kwargs):
#             my_func = fn(*args, **kwargs)
#             for _ in range(num_of_times):
#                 print(f"Hello {my_func}")
#             return my_func

#         return wrapper

#     return repeat_decorator


# @repeat(num_of_times=3)
# def name(my_name: str) -> str:
#     return my_name


# @repeat(num_of_times=5)
# def age(my_age: int) -> int:
#     return my_age


# name("Albert")
# age(5)

# =============================================================

# Create a decorator factory (decotator) that applies a given function to the result of the decorated function.
# Example, main function is to add 2 nubmers , but decorator factory is to return square of the nubmers.
# example: print(add_numbers(1,2)) returns 9 .


# from typing import Callable


# def do_pow(function: Callable) -> Callable:
#     def useless_decorator(fn: Callable):
#         def wrapper(*args, **kwargs):
#             my_func = fn(*args, **kwargs)
#             return function(my_func)

#         return wrapper

#     return useless_decorator


# def raise_square(number: int) -> int:
#     return number**2


# @do_pow(function=raise_square)
# def sum_numbers(a: int, b: int) -> int:
#     return a + b


# print(sum_numbers(1, 2))


# ==============================================================

# Create a decorator factory logging decorator that executes decorated function n given times if function raises an error.
# When function is correctly executed , logging should log to file how many times executions failed, and the result of succesfull execution.
# Create any function that could prbably fail.


from typing import Callable, Union
from random import randint
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


def repeat_n_times_or_till_success(repeat_times):
    def attempt_function(fn: Callable):
        def wrapper(*args, **kwargs):
            for i in range(repeat_times):
                try:
                    result = fn(*args, **kwargs)
                    logging.info(
                        f"Function succeeded after {i+1} attempts. Result: {result}"
                    )
                    return result
                except Exception:
                    pass

        return wrapper

    return attempt_function


@repeat_n_times_or_till_success(repeat_times=7)
def random_division(number_to_divide: Union[int, float]) -> Union[int, float]:
    return number_to_divide / randint(0, 4)


print(random_division(5))
