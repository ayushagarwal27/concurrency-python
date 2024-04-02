from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import Random

tp = ThreadPoolExecutor(max_workers=10)


def print_count(value):
    rd = Random()
    sleep(rd.random())
    print(f'Count is {value}')


for i in range(100):
    tp.submit(print_count, i)
