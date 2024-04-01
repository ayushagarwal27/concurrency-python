from threading import Thread, current_thread
from time import sleep


def task():
    sleep(1)
    print('Inside Task')
    print(current_thread().name)

t = Thread(target=task)
t.start()
print(current_thread().name)
print('Something else')
