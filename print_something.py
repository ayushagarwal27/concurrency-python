from threading import Thread
from time import sleep


class PrintSomething(Thread):
    def run(self):
        sleep(1)
        print('Print this random')

thread = PrintSomething()
thread.start()
print('Something else')