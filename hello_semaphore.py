from threading import Semaphore

sema = Semaphore(2)
print(sema.acquire())
print(sema.acquire())
print('This will execute')
print(sema.acquire())
print('This will not execute')
