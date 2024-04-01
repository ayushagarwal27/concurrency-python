from random import Random
from threading import Thread
from time import sleep


class PrintNumber(Thread):
    def __init__(self,value):
        super().__init__()
        self.value = value

    def run(self):
        r = Random()
        sleep(r.random())
        print(f'Value is {self.value}')

for i in range(100):
    printer = PrintNumber(i)
    printer.start()