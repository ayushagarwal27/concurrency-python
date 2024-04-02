from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import Random

tp = ThreadPoolExecutor(max_workers=10)


def print_count(value):
    rd = Random()
    sleep(rd.random())
    print(f'Count is {value}')
    return value ** 2


# for i in range(100):
future = tp.submit(print_count, 10)
print(future.result())
