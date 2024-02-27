# 1. Create a simple function that generates random word and returns a lentgh of that word.
# Create a decorator function that would inform if the word is short (< 6 characters) or long (>=6 chars).

# from typing import Callable
# import urllib.request
# import random


# def long_short(fn: Callable) -> str:

#     def wrapper():
#         word_length = fn()
#         if word_length < 6:
#             print("Word is short")
#         else:
#             print("Word is long")
#         return word_length

#     return wrapper


# @long_short
# def random_word_length() -> int:
#     word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
#     response = urllib.request.urlopen(word_url)
#     long_txt = response.read().decode()
#     words = long_txt.splitlines()
#     return len(random.choice(words))


# print(random_word_length())


# 2. Write a Python decorator @time_it that measures the time taken by a function to execute and prints it.


# import time
# from typing import Callable, List


# def time_it(fn: Callable) -> str:

#     def wrapper():
#         start_time = time.time()
#         my_function = fn()
#         print("--- %s seconds ---" % (time.time() - start_time))
#         return my_function

#     return wrapper


# @time_it
# def print_1000() -> None:
#     for i in range(1000):
#         print(i)


# @time_it
# def get_1000() -> List[int]:
#     my_list = [x * x for x in range(1000)]
#     return my_list


# print_1000()
# print(get_1000())


# 3. Write two decorators that would make the function output in uppercase (first) and should reverse the output string (second).
# Apply both decorators to a function that returns "hello world".

# from typing import Callable


# def do_uppercase(fn: Callable[[None], str]) -> str:

#     def wrapper():
#         reverse = fn().upper()
#         print(reverse)
#         return reverse

#     return wrapper


# def do_reverse(fn: Callable[[None], str]) -> str:

#     def wrapper():
#         reverse = fn()[::-1]
#         print(reverse)
#         return reverse

#     return wrapper


# @do_uppercase
# @do_reverse
# def hello() -> str:
#     return "hello world"


# print(hello())

# as tikejaus tokio
# dlrow olleh
# hello world
# HELLO WORLD
# hello world


# 4. Create a decorator that logs (prints and to the file) the function name, time and results every time the function is called.

import logging
from typing import Callable


logging.basicConfig(
    level=logging.INFO,
    filename="logger.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


def logger(fn: Callable) -> str:

    def wrapper():
        my_func = fn()
        logging.info(f"Function {fn.__name__!r}")
        print(f"Function {fn.__name__!r}")
        return my_func

    return wrapper


@logger
def count_smth():
    return 50 * 50


print(count_smth())
