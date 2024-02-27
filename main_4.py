# 1. Create a class with various mathematical operations (at least 5 of them), utilizing a consolidated decorator to enhance method functionalitie.
# Decorator/s must check type of the values passed to class instance methods and at the same time calcualte execution time .


# from typing import Callable
# import time


# def checker(fn: Callable):
#     def wrapper(self, *args, **kwargs):
#         start_time = time.time()
#         if all(isinstance(i, (int, float)) for i in args):
#             my_func = fn(self, *args, **kwargs)
#         else:
#             print("--- %s seconds ---" % (time.time() - start_time))
#             raise TypeError("Entered values is not numbers")
#         print("--- %s seconds ---" % (time.time() - start_time))
#         return my_func

#     return wrapper


# class Calculator:
#     @checker
#     def addition(self, a: float, b: float) -> float:
#         try:
#             return a + b
#         except Exception as err:
#             print(err)

#     @checker
#     def substraction(self, a: float, b: float) -> float:
#         return a - b

#     @checker
#     def multiplication(self, a: float, b: float) -> float:
#         return a * b

#     @checker
#     def division(self, a: float, b: float) -> float:
#         return a / b

#     @checker
#     def raise_power(self, a: float, b: float) -> float:
#         try:
#             return pow(a, b)
#         except Exception as err:
#             print(err)


# calc = Calculator()

# print(calc.raise_power(21, 51))


# 2. Create a decorator factory that would slow the execution speed of the decorated function (lets call it delay decorator.).
# Log the execution times to the file.

# import logging
# import time
# from typing import Callable

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="time_logger.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%d/%m/%Y %H:%M:%S",
# )


# def delayer(delay_time):
#     def timer(fn: Callable):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             time.sleep(delay_time)
#             my_func = fn(*args, **kwargs)
#             logging.info("Execution time: %s seconds" % (time.time() - start_time))
#             return my_func

#         return wrapper

#     return timer


# @delayer(1)
# def raise_power(a: int, b: int) -> int:
#     return pow(a, b)


# print(raise_power(5, 5))


# 3. Create a Database management class that would setup all connections and implement CRUD opearations (inside class/classses).
# There should be a decorator that would handle possible errors. 
# Please check what error hanling class SQLAlchemy provides.


