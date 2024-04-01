from random import Random
from threading import Thread
from time import sleep

def task(value):
    r = Random()
    sleep(r.random())
    print(f'Value is {value}')

for i in range(100):
    printer = Thread(target=task, args=(i,))
    printer.start()