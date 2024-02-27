# import time
# from typing import Callable, List


# def time_it(fn: Callable) -> str:

#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         my_function = fn(*args, **kwargs)
#         print("--- %s seconds ---" % (time.time() - start_time))
#         return my_function

#     return wrapper


# @time_it
# def power_fn(nr: int):
#     for i in range(nr):
#         i = i**2


# print(power_fn(nr=1000000))

# ======================================================================


# from typing import Callable


# def my_name_is(fn: Callable) -> str:

#     def wrapper(*args, **kwargs):
#         my_func = fn(*args, **kwargs)
#         print(f"My name is {my_func}")
#         return my_func

#     return wrapper


# @my_name_is
# def name(my_name: str) -> str:
#     return my_name


# print(name("Albert"))


# ======================================================================

# from typing import Callable


# def my_name_is(fn: Callable) -> str:

#     def wrapper(*args, **kwargs):
#         my_func = fn(*args, **kwargs)
#         print(f"My name is {my_func}")
#         return my_func

#     return wrapper


# class Name:
#     def __init__(self, name: str) -> None:
#         self.name = name

#     @my_name_is
#     def do_upper(self) -> str:
#         return self.name.upper()

#     @my_name_is
#     def do_reverse(self) -> str:
#         return self.name[::-1].lower()

#     @my_name_is
#     def split_to_list(self) -> str:
#         return [*self.name]


# albert = Name(name="Albert")

# print(albert.do_upper())
# print(albert.do_reverse())
# print(albert.split_to_list())

